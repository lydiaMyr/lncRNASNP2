from lncRNASNP2 import app, api
import os
import subprocess
import string
import tempfile
import shlex
from flask_restful import Resource, fields, marshal_with, reqparse, marshal
import multiprocessing
def get_tempfile_name():
    temp = tempfile.NamedTemporaryFile()
    temp.close()
    return temp.name
def miranda_pita_format(seq,file_name,prefix):
    seq = prefix+'\n'+seq
    temp_file = open(file_name, 'w')
    temp_file.write(seq)
def target_scan_format(seq, file_name, prefix):
    seq = prefix+"	"+'9606'+"	"+ seq
    temp_file = open(file_name, 'w')
    temp_file.write(seq)

def command_excute(command):
    args = shlex.split(command)
    #subprocess.check_call(args)
    with open(os.devnull, 'w') as devnull:
        subprocess.check_call(args, stdout=devnull, stderr=devnull)
def miranda_predict(seq_file,result_file):
    mirna_file = "/home/miaoyr/lncRNASNP_human/lncRNASNP2/static/lncRNASNP2/data/humam_mature.fa"
    command = "/home/miaoyr/software/miRanda-3.3a/src/miranda {mirna_file} {wild_seq_file} -en -10 -out {result_file}".format(mirna_file=mirna_file, wild_seq_file = seq_file, result_file=result_file)
    command_excute(command)
def targetscan_predict(seq_file,result_file):
    t_mirna_file = "/home/miaoyr/lncRNASNP_human/lncRNASNP2/static/lncRNASNP2/data/humam_mature_T.fasta.txt"
    command = "/home/miaoyr/software/targetscan/targetscan_70.pl {t_mirna_file} {t_fasta_file} {result_file}".format(t_mirna_file=t_mirna_file, t_fasta_file = seq_file, result_file = result_file)
    command_excute(command)

def pita_predict(seq_file, result_file):
    mirna_file = "/home/miaoyr/lncRNASNP_human/lncRNASNP2/static/lncRNASNP2/data/humam_mature.fa"
    command = "perl /home/miaoyr/software/pita/pita_prediction.pl -utr {fasta_file} -mir {mirna_file} -prefix {result_file}".format(fasta_file=seq_file, mirna_file = mirna_file, result_file = result_file)
    command_excute(command)


def result_dispose(m_result, t_result, p_result):
    result = []
    miranda_dict = {}
    t_m_dict = {}
    t_m_p_dict = {}
    with open(m_result) as reader:
        for eachline in reader:
            if eachline.startswith('>hsa'):
                s = eachline.strip().split()
                key = s[0] + '\t' + '>' + s[1]
                value = s[2:]
                miranda_dict[key] = value
    with open(t_result) as reader:
        for eachline in reader:
            s = eachline.strip().split('\t')
            key = '>' + s[1] + '\t' + s[0]
            if key in miranda_dict:
                t_m_dict[key] = s[2:]
    pita_result = p_result + "_pita_test_result.tab"
    with open(pita_result) as reader:
        for eachline in reader:
            s = eachline.strip().split('\t')
            key = '>' + s[0].split()[0] + '\t' + '>' + s[1]
            if key in t_m_dict:
                t_m_p_dict[key] = s[2:]
    for key in t_m_p_dict:
        mirna = key.split('\t')[0][1:]
        m_start = miranda_dict[key][4]
        m_end = miranda_dict[key][5]
        score = miranda_dict[key][0]
        energy = miranda_dict[key][1]
        t_start = t_m_dict[key][1]
        t_end = t_m_dict[key][2]
        p_start = t_m_p_dict[key][1]
        p_end = t_m_p_dict[key][0]
        #if int(p_end) in range(int(t_end)-5, int(t_end)+5) and int(m_end) in range(int(t_end)-5, int(t_end)+5):
        header=["mirna","m_start","m_end","t_start","t_end","p_start","p_end","score","energy"]
        content=[mirna,m_start,m_end,t_start,t_end,p_start,p_end,score,energy]
        record=dict(zip(header,content))
        result.append(record)
    os.remove(m_result)
    os.remove(t_result)
    os.remove(p_result+"_pita_test_result.tab")
    os.remove(p_result+"_ext_utr.stab")
    return result
def predict_start(seq, prefix):
    m_p_fasta = get_tempfile_name()
    t_fasta = get_tempfile_name()
    miranda_pita_format(seq, m_p_fasta, prefix)
    target_scan_format(seq, t_fasta, prefix)
    m_result = get_tempfile_name()
    t_result = get_tempfile_name()
    p_result = get_tempfile_name()
    pool = multiprocessing.Pool(processes=20)
    pool.apply_async(miranda_predict, (m_p_fasta, m_result, ))
    pool.apply_async(targetscan_predict, (t_fasta, t_result, ))
    pool.apply_async(pita_predict, (m_p_fasta, p_result, ))
    pool.close()
    pool.join()
    os.remove(m_p_fasta)
    os.remove(t_fasta)
    result = result_dispose(m_result, t_result, p_result)
    return result
def target_gain_loss(w_result,s_result):
    w_dict = {}
    s_dict = {}
    gain_ls = []
    loss_ls = []
    for record in w_result:
        w_dict[record['mirna']]=record
    for record in s_result:
        s_dict[record['mirna']]=record
    for key in s_dict:
        if not key in w_dict:
            gain_ls.append(s_dict[key])
    for key in w_dict:
        if not key in s_dict:
            loss_ls.append(w_dict[key])
    return gain_ls, loss_ls
def RNAsnp_predict(snp, seq):
    sequence=''
    seq = seq.replace('|||','\n')
    snp = snp.replace('|||','\n')
    seq_file = get_tempfile_name() 
    snp_file = get_tempfile_name()
    with open(seq_file, 'w') as writer:
        writer.write(seq)
    with open(snp_file, 'w') as writer:
        writer.write(snp)
    with open(seq_file) as reader:
        for line in reader:
            if not line.startswith('>'):
                sequence += line 
    if len(sequence)>1000:
        mode = 2
        window = 200
    else:
        mode = 1
        window = 100
    result_name = get_tempfile_name()
    result_file = open(result_name, 'w')
    os.system('/home/miaoyr/pita_file_handle/environment.sh')    
    command = "/home/miaoyr/software/RNAsnp/bin/RNAsnp -f {seq_file} -s {snp_file} -m {mode} -w {window}".format(seq_file = seq_file, snp_file = snp_file, mode = mode, window = window)
    command_excute(command)
    args = shlex.split(command)
    subprocess.check_call(args, stdout=result_file)
    result_file.close() 
    result = RNAsnp_result_dispose(result_name)
    return result 
def RNAsnp_result_dispose(result_file):
    result = []
    new = open(result_file)
    header = new.readline().strip().split('\t')
    if 'r_min' in header:
        header[6]='p_value'
        header[7]='nothing'
    else:
        header[9]='p_value'
    for eachline in new:
        context = eachline.strip().split('\t') 
        record = dict(zip(header, context))
        result.append(record)
    new.close()
    return result
class Prediction(Resource):
    def post(self):
        wild_result = []
        snp_target = []
        gain = []
        loss = []
        effect_result = []
        parser = reqparse.RequestParser()
        parser.add_argument('wild_seq')
        parser.add_argument('snp_seq')
        parser.add_argument('seq')
        parser.add_argument('snp')
        args = parser.parse_args()
        wild_seq = args['wild_seq']
        if wild_seq:
            wild_result = predict_start(wild_seq, '>wild')
        snp_seq = args['snp_seq']
        if snp_seq:
            snp_target = predict_start(snp_seq, '>snp')
            gain, loss = target_gain_loss(wild_result,snp_target) 
        RNAsnp_snp = args['snp']
        RNAsnp_seq = args['seq']
        if RNAsnp_snp and RNAsnp_seq:
            effect_result = RNAsnp_predict(RNAsnp_snp, RNAsnp_seq)
        return {'target': wild_result, 'snp_target': snp_target, 'gain': gain, 'loss': loss, 'RNAsnp': effect_result}

api.add_resource(Prediction, '/api/prediction')


