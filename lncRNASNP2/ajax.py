import flask_restful
import string
from lncRNASNP2 import app, api
from lncRNASNP2.core import mongo

from flask_restful import Resource, fields, marshal_with, reqparse, marshal

test_fields = {
    'fields1': fields.String,
    'fields2': fields.Integer,
    'fieldsx': fields.String(attribute='fields3'),
}

class FuzzyFoo(Resource):
    @marshal_with(test_fields)
    def get(self):
        a = {'fields1': 'abc', 'fields2': 1, 'fields3': 'ABC'}
        num = 10
        return a, num

api.add_resource(FuzzyFoo, '/api/test')


lncrna_snp_fields = {
    'chromosome': fields.String(attribute='chr'),
    'pos': fields.Integer,
    'lnc': fields.String,
    'snp': fields.String(attribute='dbsnp'),
    'ref_base': fields.String(attribute="r_base"),
    'alt_base': fields.String(attribute="a_base"),
    'r_fre': fields.String,
    'a_fre': fields.String,
    'target': fields.Boolean,
    'exon_start': fields.Integer(attribute='start'),
    'exon_end': fields.Integer(attribute='end'),
    'strand': fields.String,
    'tagSNP':fields.Boolean(attribute="ld"),
    'snp_count': fields.Integer,
    'gain': fields.Boolean,
    'loss':fields.Boolean,
    'effect': fields.Boolean,
    'snp_tagSNP': fields.Boolean,
    'p1':fields.String,
    'p2':fields.String,
    'GC':fields.Float,
    'd_max':fields.String,
    'r_min':fields.Float,
    'interval_1':fields.String,
    'interval_2':fields.String,
    'express': fields.Integer
}

tagSNP_fields = {
    'tagSNP': fields.String
}

ensenmbl_fields = {
    'noncode': fields.String,
    'ensembl': fields.String
}

lncrna_sequence_fields ={
    'lncrna': fields.String,
    'sequence':fields.String
}

lncrna_basic_fields = {
    'chromosome': fields.String(attribute='chr'),
    'start': fields.Integer,
    'end': fields.Integer,
    'lnc': fields.String,
    'strand': fields.String,
    'gene': fields.String,
    'snp_count': fields.Integer,
    'gain': fields.Integer,
    'loss': fields.Integer,
    'structure': fields.String,
    'cons':fields.Integer,
    'exp': fields.Integer,
    'non_cons':fields.Integer,
    'large':fields.Integer,
    'small':fields.Integer,
    'tcga_count': fields.Integer,
    'cosmic_count': fields.Integer,
    'tcga_gain':fields.Integer,
    'tcga_loss':fields.Integer,
    'cosmic_gain':fields.Integer,
    'cosmic_loss':fields.Integer,
    'express': fields.Integer
}

lncrna_gene_fileds = {
    'lncrna':fields.String(attribute="transcript"),
    'gene':fields.String,
    'snp_count': fields.Integer,
    'chromosome':fields.String(attribute='chr'),
    'gain': fields.Integer,
    'loss': fields.Integer,
    'position': fields.Integer,
    'cons':fields.Integer,
    'exp': fields.Integer,
    'non_cons':fields.Integer,
    'large':fields.Integer,
    'small':fields.Integer,
    'tcga_count': fields.Integer,
    'cosmic_count': fields.Integer,
    'tcga_gain':fields.Integer,
    'tcga_loss':fields.Integer,
    'cosmic_gain':fields.Integer,
    'cosmic_loss':fields.Integer

}

snp_basic_fields = {
    'alt_base': fields.String,
    'ref_base': fields.String,
    'snp_info': fields.String,
    'pos':fields.Integer,
    'snp_number': fields.String(attribute='dbsnp'),
    'chromosome': fields.String(attribute='chr'),
    'lnc': fields.String,
}

miR_basic_fields = {
    'mirna': fields.String(attribute='miR_ID'),
    'accession': fields.String(attribute='miR_accession'),
    'pre_mature_pos': fields.String(attribute='pre_mir_pos'),
    'pre_mature_sequence': fields.String(attribute='pre_mir_sequence'),
    'precursor': fields.String(attribute='pre_mir'),
    'strand': fields.String,
    'mature_sequence': fields.String,
    'position': fields.String,
    'expression': fields.Float,
    'chr': fields.String,
    'start': fields.Integer,
    'end': fields.Integer,
    'gain':fields.Boolean,
    'loss':fields.Boolean,
    'cons':fields.Boolean,
    'non_cons':fields.Boolean
}

miR_expression_fields = {
    'miRNA': fields.String(attribute='miR'),
    'expression': fields.Float,
}

match_mir_fields = {
    'mirna': fields.String
}

match_lncrna_fields = {
    'lncrna': fields.String,
    'gene_alias':fields.String,
    'alias':fields.String,
    'gene':fields.String,
    'transcript':fields.String,
    'trans_alias':fields.String
}


TCGA_basic_fields = {
    'snp': fields.String(attribute='dbSNP_RS'),
    'mut_info': fields.String,
    'ref_base': fields.String(attribute='Tumor_Seq_Allele1'),
    'alt_base': fields.String(attribute='Tumor_Seq_Allele2'),
    'cancer_type': fields.String,
    'Hugo_Symbol': fields.String,
    'Entrez_Gene_Id': fields.String,
    'cDNA_Change': fields.String,
    'Annotation_Transcript': fields.String,
    'Refseq_mRNA_Id': fields.String,
    'Genome_Change': fields.String,
    'Codon_Change': fields.String,
    'Protein_Change': fields.String,
    'DrugBank': fields.String,
    'SwissProt_acc_Id': fields.String,
    'GO_Biological_Process': fields.String,
    'GO_Molecular_Function': fields.String,
    'Ref_context': fields.String,
    'Other_Transcripts': fields.String,
    'chromosome': fields.String,
    'mut_start': fields.Integer,
    'mut_end': fields.Integer,
    'fre': fields.String,
    'gain':fields.Integer,
    'loss':fields.Integer,
    'target': fields.Integer
}

TCGA_lnc_fields = {
    'lncrna': fields.String(attribute='noncode_ID'),
    'start': fields.Integer,
    'end': fields.Integer,
    'strand': fields.String,
    'chromosome': fields.String(attribute='chr'),
    'mut_info': fields.String,
    'cancer_type': fields.String,
    'ID':fields.Integer,
    'mut_start':fields.Integer,
    'mut_end':fields.Integer,
    'ref_base': fields.String,
    'alt_base': fields.String,
    'effect': fields.Boolean,
    'express': fields.Boolean,
    'coding_group': fields.String,
    'coding_score':fields.Float,
    'noncoding_group': fields.String,
    'noncoding_score': fields.Float,
    'home_lnc_search_express': fields.Boolean,
    'fre': fields.String,
    'gain':fields.Integer,
    'loss':fields.Integer,
    'target': fields.Integer

}
TCGA_mut_effect_fields = {
    'cancer_type': fields.String(attribute='Cancer_type'),
    'mut_info': fields.String(attribute='Mut_info'),
    'ref_base': fields.String(attribute='Ref_base'),
    'alt_base': fields.String(attribute='Alt_base'),
    'noncoding_groups': fields.String(attribute='Noncoding_Groups'),
    'coding_groups': fields.String(attribute='Coding_Groups'),
    'coding_score': fields.Float(attribute='Coding_Score'),
    'noncoding_score': fields.Float(attribute='Noncoding_Score'),
}
lncRNA_expression_fields = {
    'gene': fields.String(attribute='lncrna'),
    'normal': fields.String,
    'tumor': fields.String,
    'lncRNA': fields.String
}

tanric_mean_fields = {
    'gene': fields.String(attribute='lncrna'),
    'normal': fields.Float,
    'cancer': fields.Float,
    'cancer_type': fields.String
}

gwas_basic_fields = {
    'snp': fields.String(attribute='SNPS'),
    'trait': fields.String(attribute='DISEASE/TRAIT'),
    'risk_allele': fields.String(attribute='RISK ALLELE'),
    'risk_allele_fre': fields.String(attribute='RISK ALLELE FREQUENCY'),
    'pubmedID': fields.String(attribute='PUBMEDID'),
    'beta': fields.String(attribute='OR or BETA'),
    'cnv': fields.String(attribute='CNV'),
    'link': fields.String(attribute='LINK'),
    'p_value': fields.String(attribute='P-VALUE'),
    'CI': fields.String(attribute='95% CI (TEXT)'),
    'study': fields.String(attribute='STUDY'),
    'mapped_gene': fields.String(attribute='MAPPED_GENE'),
}

gwas_ld_fields = {
    'tagsnp': fields.String(attribute='tagSNP'),
    'position': fields.Integer,
    'ASW_start': fields.String,
    'ASW_end': fields.String,
    'CEU_start': fields.String,
    'CEU_end': fields.String,
    'CHD_start': fields.String,
    'CHD_end': fields.String,
    'GIH_start': fields.String,
    'GIH_end': fields.String,
    'LWK_start': fields.String,
    'LWK_end': fields.String,
    'MEX_start': fields.String,
    'MEX_end': fields.String,
    'MKK_start': fields.String,
    'MKK_end': fields.String,
    'TSI_start': fields.String,
    'TSI_end': fields.String,
    'YRI_start': fields.String,
    'YRI_end': fields.String,
    'snps':fields.String(attribute='SNP'),
}

cosmic_basic_fields = {
    'position': fields.String(attribute='genome position'),
    'ref_base': fields.String(attribute='WT_SEQ'),
    'alt_base': fields.String(attribute='MUT_SEQ'),
    'somastic_status': fields.String(attribute='Mutation somatic status'),
    'pubmed_id': fields.String(attribute='PUBMED_PMID'),
    'cosmic_ncv_id': fields.String(attribute='ID_NCV'),
    'coding_groups': fields.String(attribute='FATHMM_MKL_CODING_GROUPS'),
    'coding_score': fields.Float(attribute='FATHMM_MKL_CODING_SCORE'),
    'noncoding_groups': fields.String(attribute='FATHMM_MKL_NON_CODING_GROUPS'),
    'noncoding_score': fields.Float(attribute='FATHMM_MKL_NON_CODING_SCORE'),
    'gain': fields.Integer,
    'loss': fields.Integer,
    'target': fields.Integer
}

cosmic_lnc_basic_fields = {
    'mut_info': fields.String,
    'lncrna': fields.String(attribute='lnc'),
    'start': fields.Integer(attribute='exon_start'),
    'end': fields.Integer(attribute='exon_end'),
    'chr': fields.String,
    'zygosity': fields.String,
    'ref_base': fields.String(attribute='WT_SEQ'),
    'alt_base': fields.String(attribute='MUT_SEQ'),
    'somastic_status': fields.String(attribute='Mutation somatic status'),
    'pubmed_id': fields.String(attribute='PUBMED_PMID'),
    'cosmic_cnv_id': fields.String(attribute='CNV_ID'),
    'coding_groups': fields.String(attribute='FATHMM_MKL_CODING_GROUPS'),
    'coding_score': fields.Float(attribute='FATHMM_MKL_CODING_SCORE'),
    'noncoding_groups': fields.String(attribute='FATHMM_MKL_NON_CODING_GROUPS'),
    'noncoding_score': fields.Float(attribute='FATHMM_MKL_NON_CODING_SCORE'),
    'status': fields.Boolean,
    'mut_start': fields.Integer,
    'mut_end': fields.Integer,
    'gain': fields.Integer,
    'loss': fields.Integer,
    'target': fields.Integer
}

mirna_target_fileds = {
    'lncRNA': fields.String,
    'miRNA': fields.String,
    'm_start': fields.Integer(attribute="bind_start"),
    'm_end': fields.Integer(attribute="bind_end"),
    't_start': fields.Integer,
    't_end': fields.Integer,
    'p_start': fields.Integer,
    'p_end': fields.Integer,
    'utr_start':fields.Integer,
    'utr_end': fields.Integer,
    'strand': fields.String,
    'energy': fields.Integer,
    'query': fields.String,
    'ref': fields.String,
    'detail': fields.String,
    'info': fields.String,
    'chromosome':fields.String(attribute="info_detail.chr"),
    'score': fields.Float,
    'conserve': fields.Boolean,
    'experiment': fields.Boolean,
    'large': fields.Boolean,
    'small':fields.Boolean,
    'move':fields.Integer,
    'm_move':fields.Integer
}
target_gain_fields = {
    'lncRNA': fields.String,
    'miRNA': fields.String,
    'SNP': fields.String,
    'm_start': fields.Integer(attribute="bind_start"),
    'm_end': fields.Integer(attribute="bind_end"),
    't_start': fields.Integer,
    't_end': fields.Integer,
    'strand': fields.String,
    'energy': fields.Integer,
    'query': fields.String,
    'ref': fields.String,
    'detail': fields.String,
    'info': fields.String,
    'chromosome':fields.String,
    'score': fields.Float,
}

gene_transcrit_fields = {
    'gene': fields.String,
    'chr': fields.String,
    'transcript': fields.String
}

target_loss_fields = {
    'lncRNA': fields.String,
    'miRNA': fields.String,
    'SNP': fields.String,
    'm_start': fields.Integer(attribute="bind_start"),
    'm_end': fields.Integer(attribute="bind_end"),
    't_start': fields.Integer,
    't_end': fields.Integer,
    'strand': fields.String,
    'energy': fields.Integer,
    'query': fields.String,
    'ref': fields.String,
    'detail': fields.String,
    'info': fields.String,
    'chromosome': fields.String,
    'score': fields.Float,
    'experiment': fields.Boolean
}
mirna_profile_fields = {
    'miR': fields.String,
    'Adrenocortical carcinoma': fields.String(attribute="ACC"),
    'Bladder urothelial carcinoma': fields.String(attribute="BLCA"),
    'Breast invasive carcinoma': fields.String(attribute="BRCA"),
    'Cervical and endocervical cancers': fields.String(attribute="CESC"),
    'Cholangiocarcinoma': fields.String(attribute="CHOL"),
    'Colon adenocarcinoma': fields.String(attribute="COAD"),
    'Colorectal adenocarcinom': fields.String(attribute="COADREAD"),
    'Lymphoid Neoplasm Diffuse Large B-cell Lymphoma': fields.String(attribute="DLBC"),
    'Esophageal carcinoma': fields.String(attribute="ESCA"),
    'FFPE Pilot Phase II': fields.String(attribute="FPPP"),
    'Glioblastoma multiforme': fields.String(attribute="GBM"),
    'Glioma': fields.String(attribute="GBMLGG"),
    'Head and Neck squamous cell carcinoma': fields.String(attribute="HNSC"),
    'Kidney Chromophobe': fields.String(attribute='KICH'),
    'Kidney renal clear cell carcinoma' :fields.String(attribute='KIRC'),
    'Kidney renal papillary cell carcinoma': fields.String(attribute='KIRP'),
    'Acute Myeloid Leukemia': fields.String(attribute='LAML'),
    'Brain Lower Grade Glioma': fields.String(attribute='LGG'),
    'Liver hepatocellular carcinoma': fields.String(attribute='LIHC'),
    'Lung adenocarcinoma': fields.String(attribute='LUAD'),
    'Lung squamous cell carcinoma': fields.String(attribute='LUSC'),
    'Mesothelioma': fields.String(attribute='MESO'),
    'Ovarian serous cystadenocarcinoma': fields.String(attribute="OV"),
    'Pancreatic adenocarcinoma': fields.String(attribute="PAAD"),
    'Pheochromocytoma and Paraganglioma': fields.String(attribute="PCPG"),
    'Prostate adenocarcinoma': fields.String(attribute="PRAD"),
    'Rectum adenocarcinoma': fields.String(attribute="READ"),
    'Sarcoma': fields.String(attribute="SARC"),
    'Skin Cutaneous Melanoma': fields.String(attribute='SKCM'),
    'Stomach adenocarcinoma': fields.String(attribute='STAD'),
    'Stomach and Esophageal carcinoma': fields.String(attribute='STES'),
    'Testicular Germ Cell Tumors': fields.String(attribute='TGCT'),
    'Thyroid carcinoma': fields.String(attribute='THCA'),
    'Thymoma': fields.String(attribute='THYM'),
    'Uterine Corpus Endometrial Carcinoma': fields.String(attribute='UCEC'),
    'Uterine Carcinosarcoma': fields.String(attribute='UCS'),
    'Uveal Melanoma': fields.String(attribute="UVM")
}
tracks_fields = {
    "lncrna_track": fields.String,
    "cons_track": fields.String,
    "expr_track": fields.String,
    "hexp_track": fields.String,
    "lexp_track": fields.String,
    'tracks': fields.String,
    'lncRNA':fields.String
}
ensembl_exon_fields = {
    'start': fields.Integer,
    'end': fields.Integer,
    'TransID': fields.String
}

class LncRNASNP(Resource):
    @marshal_with(lncrna_snp_fields)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('ID',type=int)
        parser.add_argument('lncrna')
        parser.add_argument('snp')
        args = parser.parse_args()
        condition={}
        if args['lncrna'] or args['snp']:
            condition = {'lnc':args['lncrna'],'snp':args['snp']}
            lncrna_snp = mongo.db.SNP_lnc_relate.find(condition)
        else:
            lncrna_snp = mongo.db.SNP_lnc_relate.find_one()

        app.logger.debug("lncrna_snp={}".format(lncrna_snp))
        return lncrna_snp

api.add_resource(LncRNASNP, '/api/lncrna_snp')

ensembl_exon_list_fields = {
    'ensembl_list': fields.List(fields.Nested(ensembl_exon_fields))
}

lncrna_snp_list_fields = {
    'lncrna_snp_list': fields.List(fields.Nested(lncrna_snp_fields)),
    'records_number': fields.Integer,

}

ensenmbl_list_fields = {
    'ensenmbl_list': fields.List(fields.Nested(ensenmbl_fields))
}
lncrna_gene_list_fields = {
    'lncrna_gene_list': fields.List(fields.Nested(lncrna_gene_fileds)),
    'records_number': fields.Integer
}

lncrna_basic_list_fields = {
    'lncrna_basic_list': fields.List(fields.Nested(lncrna_basic_fields)),
    'records_number': fields.Integer,
    'gene_alias':fields.String,
    'trans_alias':fields.String,
    'pubmed':fields.String,
}

snp_basic_list_fields = {
    'snp_basic_list': fields.List(fields.Nested(snp_basic_fields))
}

miR_basic_list_fields = {
    'miR_basic_list': fields.List(fields.Nested(miR_basic_fields)),
    'records_number': fields.Integer
}
match_mir_list_fields = {
    'match_result': fields.List(fields.Nested(match_mir_fields))
}

match_lncrna_list_fields = {
    'match_result': fields.List(fields.Nested(match_lncrna_fields))
}

miR_exp_list_fields = {
    'hmirna_list': fields.List(fields.Nested(miR_expression_fields)),
    'mmirna_list': fields.List(fields.Nested(miR_expression_fields)),
    'lmirna_list': fields.List(fields.Nested(miR_expression_fields)),
    'vmirna_list': fields.List(fields.Nested(miR_expression_fields))
}

miR_profile_list_fields = {
    'mirna_profile': fields.List(fields.Nested(mirna_profile_fields))
}

TCGA_basic_list_fields = {
    'TCGA_basic_list': fields.List(fields.Nested(TCGA_basic_fields))
}

TCGA_lnc_list_fields = {
    'TCGA_lnc_list': fields.List(fields.Nested(TCGA_lnc_fields)),
    'records_number': fields.Integer,
    'tanric': fields.Boolean
}

lncRNA_exoression_list_fields = {
    'lncRNA_expression_list': fields.List(fields.Nested(lncRNA_expression_fields)),
}
tanric_mean_list_fields = {
    'lncRNA_expression_mean_list': fields.List(fields.Nested(tanric_mean_fields)),
}

TCGA_mut_effect_list_fields = {
    'TCGA_mut_effect_list': fields.List(fields.Nested(TCGA_mut_effect_fields))
}

gwas_basic_list_fields = {
    'gwas_basic_list': fields.List(fields.Nested(gwas_basic_fields))
}

gwas_ld_list_fields = {
    'gwas_ld_list': fields.List(fields.Nested(gwas_ld_fields)),
    'tagSNP_list': fields.List(fields.Nested(tagSNP_fields))
}

cosmic_basic_list_fields = {
    'cosmic_basic_list': fields.List(fields.Nested(cosmic_basic_fields))
}

cosmic_lnc_list_fields = {
    'cosmic_lnc_list': fields.List(fields.Nested(cosmic_lnc_basic_fields)),
    'records_number': fields.Integer
}
target_gain_list_fields = {
    'target_gain_list': fields.List(fields.Nested(target_gain_fields)),
    'records_gain': fields.Integer
}

gene_transcrit_list_fields = {
    'transcripts_list': fields.List(fields.Nested(gene_transcrit_fields)),
}

target_loss_list_fields = {
    'target_loss_list': fields.List(fields.Nested(target_loss_fields)),
    'records_loss': fields.Integer
}
mirna_target_list_fields = {
    'cons_target_ls': fields.List(fields.Nested(mirna_target_fileds)),
    'non_cons_target_ls': fields.List(fields.Nested(mirna_target_fileds)),
    'cons_ls': fields.List(fields.Nested(mirna_target_fileds)),
    'exp_ls':fields.List(fields.Nested(mirna_target_fileds)),
    'large_ls':fields.List(fields.Nested(mirna_target_fileds)),
    'small_ls':fields.List(fields.Nested(mirna_target_fileds)),
    'exon_start':fields.Integer,
    'cons_records_number': fields.Integer,
    'non_cons_records_number': fields.Integer,
    'target': fields.List(fields.Nested(mirna_target_fileds)),
}

lncrna_sequence_list_fileds = {
    'lncrna_sequence_list': fields.List(fields.Nested(lncrna_sequence_fields))
}
class TCGATargetGainList(Resource):
    @marshal_with(target_gain_list_fields)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int, default=1)
        parser.add_argument('per_page', type=int, default=5)
        parser.add_argument('snp')
        parser.add_argument('miRNA')
        parser.add_argument('lncrna')
        args = parser.parse_args()
        page = args['page']
        per_page = args['per_page']
        record_skip = (page - 1) * per_page
        condition = {}
        mongo.db.tcga_target_gain.ensure_index("SNP")
        mongo.db.tcga_target_gain.ensure_index("miRNA")
        mongo.db.tcga_target_gain.ensure_index("lncRNA")
        mongo.db.lncrna_chr.ensure_index("lnc")
        if args['snp']:
            target_key = string.join(args['snp'].split(';')[0:3], '_') + ';' + string.join(args['snp'].split(';')[3:5], ';')
            condition = {'SNP':target_key}
        if args['miRNA']:
            condition['miRNA'] = args['miRNA']
        if args['lncrna']:
            lnc_name=''
            if "ENST" in args['lncrna']:
                noncode = mongo.db.noncode_esenmbl.find_one({"ensembl":args['lncrna']})
                lnc_name=noncode["noncode"]
            else:
                lnc_name=args['lncrna']
            if not '.' in lnc_name:
                condition['lncRNA'] = {"$regex": lnc_name, "$options": "$i"}
            else:
                condition['lncRNA'] = lnc_name
        all_info = []
        target_gain_list = list(mongo.db.tcga_target_gain.find(condition).sort([("score",-1)]))
        records_gain = mongo.db.tcga_target_gain.find(condition).count()
        for item in target_gain_list:
            lnc = item["lncRNA"]
            query = item["query"]
            ref = item["ref"]
            detail = item["detail"]
            item["query"] = 'miRNA: ' + str(query)[13:]
            item["ref"] = 'lncRNA:' + str(ref)[13:]
            item["detail"] = str(detail)[6:]
            lnc_info = mongo.db.lncrna_chr.find_one({"lnc":lnc})
            item['chromosome'] = lnc_info["chr"]
            all_info.append(item)
        return {"target_gain_list": all_info,"records_gain":records_gain}
api.add_resource(TCGATargetGainList,'/api/tcga_target_gain_list')

class TCGATargetLossList(Resource):
    @marshal_with(target_loss_list_fields)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('snp')
        parser.add_argument('miRNA')
        parser.add_argument('lncrna')
        parser.add_argument('page', type=int, default=1)
        parser.add_argument('per_page', type=int, default=5)
        args = parser.parse_args()
        page = args['page']
        per_page = args['per_page']
        record_skip = (page - 1) * per_page
        mongo.db.tcga_target_loss.ensure_index("SNP")
        mongo.db.tcga_target_loss.ensure_index("miRNA")
        mongo.db.tcga_target_loss.ensure_index("lncRNA")
        condition = {}
        if args['snp']:
            target_key = string.join(args['snp'].split(';')[0:3], '_') + ';' + string.join(args['snp'].split(';')[3:5],';')
            condition = {'SNP': target_key}
        if args['miRNA']:
            condition['miRNA'] = args['miRNA']
        if args['lncrna']:
            lnc_name=''
            if "ENST" in args['lncrna']:
                noncode = mongo.db.noncode_esenmbl.find_one({"ensembl":args['lncrna']})
                lnc_name=noncode["noncode"]
            else:
                lnc_name=args['lncrna']
            if not '.' in lnc_name:
                condition['lncRNA'] = {"$regex": lnc_name, "$options": "$i"}
            else:
                condition['lncRNA'] = lnc_name
        target_loss_list = mongo.db.tcga_target_loss.find(condition).sort([("score",-1)])
        records_loss = mongo.db.tcga_target_loss.find(condition).count()
        all_info = []
        for item in target_loss_list:
            lnc = item["lncRNA"]
            query = item["query"]
            ref = item["ref"]
            detail = item["detail"]
            item['experiment'] = int(item['experiment'])
            item["query"] = 'miRNA: '+str(query)[13:]
            item["ref"] = 'lncRNA:'+str(ref)[13:]
            item["detail"] = str(detail)[6:]
            lnc_info = mongo.db.lncrna_chr.find_one({"lnc":lnc})
            item['chromosome'] = lnc_info["chr"]
            all_info.append(item)
        return {"target_loss_list": all_info,"records_loss":records_loss}
api.add_resource(TCGATargetLossList,'/api/tcga_target_loss_list')

class CosmicTargetGainList(Resource):
    @marshal_with(target_gain_list_fields)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int, default=1)
        parser.add_argument('per_page', type=int, default=5)
        parser.add_argument('snp')
        parser.add_argument('miRNA')
        parser.add_argument('lncrna')
        args = parser.parse_args()
        page = args['page']
        per_page = args['per_page']
        record_skip = (page - 1) * per_page
        condition = {}
        mongo.db.cosmic_target_gain.ensure_index("SNP")
        mongo.db.cosmic_target_gain.ensure_index("miRNA")
        mongo.db.cosmic_target_gain.ensure_index("lncRNA")
        mongo.db.lncrna_chr.ensure_index("lnc")
        if args['snp']:
            condition["SNP"]={"$regex": args["snp"], "$options": "$i"}
        if args['miRNA']:
            condition['miRNA'] = args['miRNA']
        if args['lncrna']:
            lnc_name=''
            if "ENST" in args['lncrna']:
                noncode = mongo.db.noncode_esenmbl.find_one({"ensembl":args['lncrna']})
                lnc_name=noncode["noncode"]
            else:
                lnc_name=args['lncrna']
            if not '.' in lnc_name:
                condition['lncRNA'] = {"$regex": lnc_name, "$options": "$i"}
            else:
                condition['lncRNA'] = lnc_name
        all_info = []
        target_gain_list = list(mongo.db.cosmic_target_gain.find(condition).sort([("score",-1)]))
        records_gain = mongo.db.cosmic_target_gain.find(condition).count()
        for item in target_gain_list:
            lnc = item["lncRNA"]
            query = item["query"]
            ref = item["ref"]
            detail = item["detail"]
            item["query"] = 'miRNA: ' + str(query)[13:]
            item["ref"] = 'lncRNA:' + str(ref)[13:]
            item["detail"] = str(detail)[6:]
            lnc_info = mongo.db.lncrna_chr.find_one({"lnc":lnc})
            item['chromosome'] = lnc_info["chr"]
            all_info.append(item)
        return {"target_gain_list": all_info,"records_gain":records_gain}
api.add_resource(CosmicTargetGainList,'/api/cosmic_target_gain_list')

class CosmicTargetLossList(Resource):
    @marshal_with(target_loss_list_fields)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('snp')
        parser.add_argument('miRNA')
        parser.add_argument('lncrna')
        parser.add_argument('page', type=int, default=1)
        parser.add_argument('per_page', type=int, default=5)
        args = parser.parse_args()
        page = args['page']
        per_page = args['per_page']
        record_skip = (page - 1) * per_page
        mongo.db.cosmic_target_loss.ensure_index("SNP")
        mongo.db.cosmic_target_loss.ensure_index("miRNA")
        mongo.db.cosmic_target_loss.ensure_index("lncRNA")
        condition = {}
        if args['snp']:
            condition["SNP"] = {"$regex": args["snp"], "$options": "$i"}
        if args['miRNA']:
            condition['miRNA'] = args['miRNA']
        if args['lncrna']:
            lnc_name=''
            if "ENST" in args['lncrna']:
                noncode = mongo.db.noncode_esenmbl.find_one({"ensembl":args['lncrna']})
                lnc_name=noncode["noncode"]
            else:
                lnc_name=args['lncrna']
            if not '.' in lnc_name:
                condition['lncRNA'] = {"$regex": lnc_name, "$options": "$i"}
            else:
                condition['lncRNA'] = lnc_name
        target_loss_list = mongo.db.cosmic_target_loss.find(condition).sort([("score",-1)])
        records_loss = mongo.db.cosmic_target_loss.find(condition).count()
        all_info = []
        for item in target_loss_list:
            lnc = item["lncRNA"]
            query = item["query"]
            ref = item["ref"]
            detail = item["detail"]
            item['experiment'] = int(item['experiment'])
            item["query"] = 'miRNA: '+str(query)[13:]
            item["ref"] = 'lncRNA:'+str(ref)[13:]
            item["detail"] = str(detail)[6:]
            lnc_info = mongo.db.lncrna_chr.find_one({"lnc":lnc})
            item['chromosome'] = lnc_info["chr"]
            all_info.append(item)
        return {"target_loss_list": all_info,"records_loss":records_loss}
api.add_resource(CosmicTargetLossList,'/api/cosmic_target_loss_list')

class GeneTranscriptList(Resource):
    @marshal_with(gene_transcrit_list_fields)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('gene')
        args = parser.parse_args()
        condition={}
        transcript_list = []
        if "NONH" in args['gene']:
            condition['gene'] ={"$regex":args['gene'],"$options":"$i"}
            transcript_list = mongo.db.lncRNA_gene_transcript.find(condition)
        else:
            condition = {'alias': {"$regex": args['gene'], "$options": "$i"}}
            lncrna_info = mongo.db.NONCODE_alias.find(condition)
            for item in lncrna_info:
                alias = item['alias']
                gene_alias = '-'
                trans_alias = '-'
                if ';' in alias:
                    gene_alias = alias.split(';')[0]
                    trans_alias = alias.split(';')[1]
                else:
                    trans_alias = alias
                item['gene_alias'] = gene_alias
                item['trans_alias'] = trans_alias
                transcript_list.append(item)

        return {'transcripts_list':list(transcript_list)}
api.add_resource(GeneTranscriptList,'/api/gene')

class MatchMirnaList(Resource):
    @marshal_with(match_mir_list_fields)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('mirna')
        args = parser.parse_args()
        condition = {}
        combine_ls=[]
        if args['mirna']:
            condition={'miR_ID':{"$regex":args['mirna'],"$options":"$i"}}
        mirna_info = mongo.db.miR_basic_info.find(condition)
        for item in mirna_info:
            combine_ls.append({"mirna":item["miR_ID"]})
        return {"match_result":combine_ls}
api.add_resource(MatchMirnaList, '/api/match_result')

class MatchLncrnaList(Resource):
    @marshal_with(match_lncrna_list_fields)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('lncrna')
        args = parser.parse_args()
        condition = {}
        combine_ls=[]
        if 'NONH' in args['lncrna']:
            condition={'lncrna':{"$regex":args['lncrna'],"$options":"$i"}}
            lncrna_info = mongo.db.lncrna_structure.find(condition)
            for item in lncrna_info:
                combine_ls.append({"lncrna": item["lncrna"]})
        else:
            condition = {'alias': {"$regex": args['lncrna'], "$options": "$i"}}
            lncrna_info = mongo.db.NONCODE_alias.find(condition)
            for item in lncrna_info:
                alias = item['alias']
                gene_alias='-'
                if ';' in alias:
                    gene_alias = alias.split(';')[0]
                    trans_alias = alias.split(';')[1]
                else:
                    trans_alias=alias
                item['gene_alias']= gene_alias
                item['trans_alias'] = trans_alias
                combine_ls.append(item)
        return {"match_result":combine_ls}
api.add_resource(MatchLncrnaList, '/api/lncrna_match_result')


class LncrnaMirnaBindingTracksAPI(Resource):
    @marshal_with(tracks_fields)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('lncrna')
        args = parser.parse_args()
        condition={}
        if args['lncrna']:
            if "ENST" in args['lncrna']:
                noncode = mongo.db.noncode_esenmbl.find_one({"ensembl": args['lncrna']})
                lnc_name = noncode["noncode"]
            else:
                lnc_name = args['lncrna']
            condition["lncRNA"] = lnc_name
        tracks = mongo.db.human_lncrna_binding_mirnas_tracks.find_one(condition)
        return tracks
api.add_resource(LncrnaMirnaBindingTracksAPI, '/api/tracks')


class LncrnaSequenceList(Resource):
    @marshal_with(lncrna_sequence_list_fileds)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('lncrna')
        args = parser.parse_args()
        condition = {}
        if args['lncrna']:
            condition["lncrna"] = args['lncrna']
        sequence = list(mongo.db.lncrna_sequence.find(condition))
        return {"lncrna_sequence_list":sequence}
api.add_resource(LncrnaSequenceList,'/api/lncrna_sequence')

class MirnaTargetList(Resource):
    @marshal_with(mirna_target_list_fields)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('snp')
        parser.add_argument('mirna')
        parser.add_argument('lncrna')
        parser.add_argument('t_start')
        parser.add_argument('cons_page', type=int, default=1)
        parser.add_argument('non_cons_page', type=int, default=1)
        parser.add_argument('per_page', type=int, default=5)
        args = parser.parse_args()
        cons_page = args['cons_page']
        non_cons_page = args['non_cons_page']
        per_page = args['per_page']
        cons_record_skip = (cons_page - 1) * per_page
        non_cons_record_skip = (non_cons_page - 1) * per_page
        condition_cons = {}
        condition_non_cons = {}
        mongo.db.human_target.ensure_index("experiment")
        mongo.db.human_target.ensure_index("conserve")
        mongo.db.human_target.ensure_index("t_start")
        mongo.db.humna_target.ensure_index("miRNA")
        mongo.db.human_target.ensure_index("lncRNA")
        mongo.db.miRNA_expression.ensure_index("expression")
        cons_ls=[]
        non_cons_ls=[]
        condition = {}
        target_info=''
        cons_records_number = 0
        non_cons_records_number = 0
        if args['mirna']:
            condition_cons['miRNA'] = args['mirna']
            condition_non_cons['miRNA'] = args['mirna']
            condition['miRNA'] = args['mirna']
        if args['lncrna']:
            if "ENST" in args['lncrna']:
                noncode = mongo.db.noncode_esenmbl.find_one({"ensembl":args['lncrna']})
                lnc_name=noncode["noncode"]
            else:
                lnc_name=args['lncrna']
            condition_cons['lncRNA'] = lnc_name
            condition['lncRNA'] = lnc_name
            if not '.' in lnc_name:
                condition_non_cons['lncRNA'] = {"$regex": lnc_name, "$options": "$i"}
            else:
                condition_non_cons['lncRNA'] = lnc_name
        if not args['t_start']:
            condition_cons["conserve"] = 1
            condition_non_cons["conserve"] = 0
            # cons_target_ls=mongo.db.mouse_target.find(cons_condition)
            all_target_ls = mongo.db.mouse_target.find(condition)
            cons_target_ls = mongo.db.human_target.aggregate([{"$match": condition_cons}, {
                "$lookup": {"from": "lncrna_chr", "localField": "lncRNA", "foreignField": "lnc",
                            "as": "info_detail"}}, {"$unwind": "$info_detail"}])
            for item in cons_target_ls:
                query = item["query"]
                ref = item["ref"]
                detail = item["detail"]
                item["query"] = 'miRNA: ' + str(query)[13:]
                item["ref"] = 'lncRNA:' + str(ref)[13:]
                item["detail"] = str(detail)[6:]
                cons_ls.append(item)
            cons_records_number = mongo.db.human_target.find(condition_cons).count()
            non_cons_target_ls = mongo.db.human_target.aggregate([{"$match": condition_non_cons}, {
                "$lookup": {"from": "lncrna_chr", "localField": "lncRNA", "foreignField": "lnc",
                            "as": "info_detail"}}, {"$unwind": "$info_detail"}, {"$limit":50}])
            for item in non_cons_target_ls:
                query = item["query"]
                ref = item["ref"]
                detail = item["detail"]
                item["query"] = 'miRNA: ' + str(query)[13:]
                item["ref"] = 'lncRNA:' + str(ref)[13:]
                item["detail"] = str(detail)[6:]
                non_cons_ls.append(item)
            non_cons_records_number = mongo.db.human_target.find(condition_non_cons).count()
        else:
            condition = {'miRNA':'hsa-'+args['mirna'],'lncRNA':args['lncrna'],'t_start':int(args['t_start'])}
            target_info = mongo.db.human_target.find_one(condition)
            query = target_info["query"]
            ref = target_info["ref"]
            detail = target_info["detail"]
            target_info["query"] = 'miRNA: ' + str(query)[13:]
            target_info["ref"] = 'lncRNA:' + str(ref)[13:]
            target_info["detail"] = str(detail)[6:]
        return {"target":target_info,"cons_target_ls":cons_ls,"non_cons_target_ls":non_cons_ls, "cons_records_number":cons_records_number,"non_cons_records_number":non_cons_records_number}
api.add_resource(MirnaTargetList,'/api/mirna_target_list')


class EnsenmblList(Resource):
    @marshal_with(ensenmbl_list_fields)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('ensenmbl')
        parser.add_argument('noncode')
        args = parser.parse_args()
        condition={}
        if args['ensenmbl']:
            condition={'ensembl':args['ensenmbl']}
        noncode_name = mongo.db.noncode_esenmbl.find_one(condition)
        return {"ensenmbl_list":noncode_name}
api.add_resource(EnsenmblList,'/api/ensembl_list')

class TargetGainList(Resource):
    @marshal_with(target_gain_list_fields)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int, default=1)
        parser.add_argument('per_page', type=int, default=5)
        parser.add_argument('snp')
        parser.add_argument('miRNA')
        parser.add_argument('lncrna')
        args = parser.parse_args()
        page = args['page']
        per_page = args['per_page']
        record_skip = (page - 1) * per_page
        condition = {}
        mongo.db.target_gain.ensure_index("SNP")
        mongo.db.target_gain.ensure_index("miRNA")
        mongo.db.target_gain.ensure_index("lncRNA")
        mongo.db.lncrna_chr.ensure_index("lnc")
        if args['snp']:
            condition = {'SNP':args['snp']}
        if args['miRNA']:
            condition['miRNA'] = args['miRNA']
        if args['lncrna']:
            lnc_name=''
            if "ENST" in args['lncrna']:
                noncode = mongo.db.noncode_esenmbl.find_one({"ensembl":args['lncrna']})
                lnc_name=noncode["noncode"]
            else:
                lnc_name=args['lncrna']
            if not '.' in lnc_name:
                condition['lncRNA'] = {"$regex": lnc_name, "$options": "$i"}
            else:
                condition['lncRNA'] = lnc_name
        all_info = []
        if not args['miRNA']:
            target_gain_list = list(mongo.db.target_gain.find(condition))
        else:
            target_gain_list = list(mongo.db.target_gain.find(condition).limit(50).sort([("score", -1)]))
        records_gain = mongo.db.target_gain.find(condition).count()
        for item in target_gain_list:
            lnc = item["lncRNA"]
            query = item["query"]
            ref = item["ref"]
            detail = item["detail"]
            item["query"] = 'miRNA: ' + str(query)[13:]
            item["ref"] = 'lncRNA:' + str(ref)[13:]
            item["detail"] = str(detail)[6:]
            lnc_info = mongo.db.lncrna_chr.find_one({"lnc":lnc})
            item['chromosome'] = lnc_info["chr"]
            all_info.append(item)
        return {"target_gain_list": all_info,"records_gain":records_gain}
api.add_resource(TargetGainList,'/api/target_gain_list')

class TargetLossList(Resource):
    @marshal_with(target_loss_list_fields)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('snp')
        parser.add_argument('miRNA')
        parser.add_argument('lncrna')
        parser.add_argument('page', type=int, default=1)
        parser.add_argument('per_page', type=int, default=5)
        args = parser.parse_args()
        page = args['page']
        per_page = args['per_page']
        record_skip = (page - 1) * per_page
        mongo.db.target_loss.ensure_index("SNP")
        mongo.db.target_loss.ensure_index("miRNA")
        mongo.db.target_loss.ensure_index("lncRNA")
        condition = {}
        if args['snp']:
            condition = {'SNP': args['snp']}
        if args['miRNA']:
            condition['miRNA'] = args['miRNA']
        if args['lncrna']:
            lnc_name=''
            if "ENST" in args['lncrna']:
                noncode = mongo.db.noncode_esenmbl.find_one({"ensembl":args['lncrna']})
                lnc_name=noncode["noncode"]
            else:
                lnc_name=args['lncrna']
            if not '.' in lnc_name:
                condition['lncRNA'] = {"$regex": lnc_name, "$options": "$i"}
            else:
                condition['lncRNA'] = lnc_name
        if not args['miRNA']:
            target_loss_list = list(mongo.db.target_loss.find(condition))
        else:
            target_loss_list = list(mongo.db.target_loss.find(condition).limit(50).sort([("score", -1)]))
        records_gain = mongo.db.target_gain.find(condition).count()
        records_loss = mongo.db.target_loss.find(condition).count()
        all_info = []
        for item in target_loss_list:
            lnc = item["lncRNA"]
            query = item["query"]
            ref = item["ref"]
            detail = item["detail"]
            item['experiment'] = int(item['experiment'])
            item["query"] = 'miRNA: '+str(query)[13:]
            item["ref"] = 'lncRNA:'+str(ref)[13:]
            item["detail"] = str(detail)[6:]
            lnc_info = mongo.db.lncrna_chr.find_one({"lnc":lnc})
            item['chromosome'] = lnc_info["chr"]
            all_info.append(item)
        return {"target_loss_list": all_info,"records_loss":records_loss}
api.add_resource(TargetLossList,'/api/target_loss_list')

class LncRNAExpressionMeanList(Resource):
    @marshal_with(tanric_mean_list_fields)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('lncRNA')
        args = parser.parse_args()
        mongo.db.lncrna_expression_mean.ensure_index("lncrna")
        mongo.db.noncode_esenmbl.ensure_index("ensembl")
        mongo.db.lncRNA_gene_transcript.ensure_index("transcript")
        condition = {}
        if args['lncRNA']:
            lnc_name=''
            if "ENST" in args['lncRNA']:
                noncode = mongo.db.noncode_esenmbl.find_one({"ensembl":args['lncRNA']})
                lnc_name=noncode["noncode"]
            else:
                lnc_name=args['lncRNA']
            gene_name = mongo.db.lncRNA_gene_transcript.find_one({"transcript": lnc_name})
            condition['lncrna'] = gene_name['gene']
        print condition
        lncrna_expression_mean_list = list(mongo.db.lncrna_expression_mean.find(condition).sort([("cancer_type",1)]))
        # print lncrna_expression_mean_list
        return {"lncRNA_expression_mean_list":lncrna_expression_mean_list}
api.add_resource(LncRNAExpressionMeanList,'/api/lncrna_express_mean')

class LncRNAExpressionList(Resource):
    @marshal_with(lncRNA_exoression_list_fields)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('lncRNA')
        parser.add_argument('cancer',type=str, default="BLCA")
        args = parser.parse_args()
        mongo.db.lncrna_expression.ensure_index("lncrna")
        mongo.db.lncrna_expression.ensure_index("cancer")
        condition = {}
        express_gene=""
        if not args['cancer']=="null":
            condition['cancer'] = args['cancer']
        if args['lncRNA']:
            lnc_name=''
            if "ENST" in args['lncRNA']:
                noncode = mongo.db.noncode_esenmbl.find_one({"ensembl":args['lncrna']})
                lnc_name=noncode["noncode"]
            else:
                lnc_name=args['lncRNA']
            gene_name = mongo.db.lncRNA_gene_transcript.find_one({"transcript": lnc_name})
            condition['lncrna'] = gene_name['gene']
            express_gene=gene_name['gene']
        lncrna_expression_list = list(mongo.db.lncrna_expression.find(condition))
        if args['cancer'] == "GBM":
            lncrna_express2 = list(mongo.db.lncrna_expression.find({'cancer': "GBM_CHINA", "lncrna": express_gene}))
            lncrna_expression_list.extend(lncrna_express2)
        if args['cancer'] == "LUAD":
            lncrna_express2 = list(mongo.db.lncrna_expression.find({'cancer': "LUAD_KOREA", "lncrna": express_gene}))
            lncrna_expression_list.extend(lncrna_express2)
        return {"lncRNA_expression_list":lncrna_expression_list}
api.add_resource(LncRNAExpressionList,'/api/lncrna_expression_list')

class lncRNABasicList(Resource):
    @marshal_with(lncrna_basic_list_fields)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int, default=1)
        parser.add_argument('per_page', type=int, default=15)
        parser.add_argument('lncrna')
        parser.add_argument('chromosome',type=str, default="chr1")
        args = parser.parse_args()
        page = args['page']
        per_page = args['per_page']
        record_skip = (page - 1) * per_page
        condition={}
        gene_alias=''
        trans_alias=''
        pubmed=''
        mongo.db.NONCODE_alias.ensure_index('transcript')
        if args['lncrna']:
            lnc_name=''
            if "ENST" in args['lncrna']:
                noncode = mongo.db.noncode_esenmbl.find_one({"ensembl":args['lncrna']})
                lnc_name=noncode["noncode"]
            else:
                lnc_name=args['lncrna']
            condition = {'lnc':lnc_name}
            alias = mongo.db.NONCODE_alias.find_one({'transcript':lnc_name})
            if alias['gene']:
                gene_a,trans_a = alias['alias'].strip().split(';')
                gene_alias = str(gene_a)
                trans_alias = str(trans_a)
            else:
                trans_alias = alias['alias'].strip()
            if "pubmed" in alias:
                pubmed = alias['pubmed']
        mongo.db.lncRNA_transcript_basic_info.ensure_index("lnc")
        mongo.db.lncRNA_transcript_basic_info.ensure_index("chr")
        mongo.db.lncRNA_gene_transcript.ensure_index("transcript")
        mongo.db.SNP_lnc_relate.ensure_index("lnc")
        mongo.db.lncrna_structure.ensure_index('lncrna')
        mongo.db.TCGA_lnc_relate.ensure_index("noncode_ID")
        mongo.db.cosmic_mut_in_lnc.ensure_index("lnc")
        mongo.db.target_gain.ensure_index("lncRNA")
        mongo.db.target_loss.ensure_index("lncRNA")
        mongo.db.tcga_target_gain.ensure_index("lncRNA")
        mongo.db.tcga_target_loss.ensure_index("lncRNA")
        mongo.db.cosmic_target_gain.ensure_index("lncRNA")
        mongo.db.cosmic_target_loss.ensure_index("lncRNA")
        lnc_gene = list(mongo.db.lncRNA_transcript_basic_info.aggregate([{"$match":condition},{"$lookup":{"from":"lncRNA_gene_transcript","localField":"lnc","foreignField":"transcript","as":"info_detail"}},{"$unwind":"$info_detail"}])) #snp_count = mongo.db.SNP_lnc_relate.aggregate(([{"$group": {"_id": "$lnc", "count": {"$sum":1}}},{"$find":{"_id":"NONHSAT011370.2"}}]))
        #print list(snp_count)
        combine_ls = []
        for temp in lnc_gene:
            info = temp["info_detail"]
            temp["gene"] = info["gene"]
            lnc = temp['lnc']
            gene_ls = list(mongo.db.lncRNA_gene_transcript.find({"transcript": lnc}))
            gene = gene_ls[0]["gene"]
            express = mongo.db.lncrna_expression.find({"lncrna": str(gene)}).count()
            target_ls = mongo.db.human_target.find({"lncRNA": lnc})
            cons = 0
            non_cons = 0
            exp = 0
            large = 0
            small = 0
            tcga_count = mongo.db.TCGA_lnc_relate.find({"noncode_ID": lnc}).count()
            cosmic_count = mongo.db.cosmic_mut_in_lnc.find({"lnc":lnc}).count()
            tcga_gain = mongo.db.tcga_target_gain.find({"lncRNA": lnc}).count()
            tcga_loss = mongo.db.tcga_target_loss.find({"lncRNA": lnc}).count()
            cosmic_gain = mongo.db.cosmic_target_gain.find({"lncRNA": lnc}).count()
            cosmic_loss = mongo.db.cosmic_target_loss.find({"lncRNA": lnc}).count()
            temp['tcga_count'] = tcga_count
            temp['cosmic_count'] = cosmic_count
            temp['tcga_gain'] = tcga_gain
            temp['tcga_loss'] = tcga_loss
            temp['express'] = express
            temp['cosmic_gain'] = cosmic_gain
            temp['cosmic_loss'] = cosmic_loss
            for target in target_ls:
                cons_tag = target['conserve']
                exp_tag = target['experiment']
                mirna = target['miRNA']
                expression = target["expression"]
                if cons_tag == 1:
                    cons += 1
                else:
                    non_cons += 1
                if exp_tag == 1:
                    exp += 1
                if expression >= 1:
                    large += 1
                else:
                    small += 1
            temp['cons'] = cons
            temp['non_cons'] = non_cons
            temp['large'] = large
            temp['small'] = small
            temp['exp'] = exp
            gain = mongo.db.target_gain.find({'lncRNA': lnc}).count()
            loss = mongo.db.target_loss.find({'lncRNA': lnc}).count()
            structure = list(mongo.db.lncrna_structure.find({'lncrna':lnc}))
            temp["structure"] = structure[0]["structure"]
            temp['gain'] = gain
            temp['loss'] = loss
            count = mongo.db.SNP_lnc_relate.find({'lnc': str(lnc)}).count()
            temp['snp_count'] = count
            combine_ls.append(temp)
        return {'lncrna_basic_list': combine_ls,'gene_alias':gene_alias,'trans_alias':trans_alias,'pubmed':pubmed}
api.add_resource(lncRNABasicList,'/api/lncrna_basic_list')

class LncGeneList(Resource):
    @marshal_with(lncrna_gene_list_fields)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int, default=1)
        parser.add_argument('per_page', type=int, default=15)
        parser.add_argument('lncrna')
        parser.add_argument('chromosome', type=str, default="chr1")
        args = parser.parse_args()
        page = args['page']
        per_page = args['per_page']
        record_skip = (page - 1) * per_page
        condition = {'chr':args['chromosome']}
        records_number = mongo.db.lncRNA_gene_transcript.find({'chr':args['chromosome']}).count()
        if args['lncrna']:
            if not ',' in args['lncrna']:
                if "ENST" in args['lncrna']:
                    noncode = mongo.db.noncode_esenmbl.find_one({"ensembl":args['lncrna']})
                    lnc_name=noncode["noncode"]
                else:
                    lnc_name=args['lncrna']
                    condition = {'transcript':lnc_name}
            else:
                lncrna_ls = args['lncrna'].split(',')
                ls = []
                for lncrna in lncrna_ls:
                    if "ENST" in lncrna:
                        noncode = mongo.db.noncode_esenmbl.find_one({"ensembl": lncrna})
                        lnc_name = noncode["noncode"]
                    else:
                        lnc_name = lncrna
                    ls.append({"transcript": lnc_name})
                condition = {"$or": ls}
        mongo.db.lncRNA_gene_transcript.ensure_index("transcript")
        mongo.db.lncRNA_gene_transcript.ensure_index("gene")
        mongo.db.SNP_lnc_relate.ensure_index("lnc")
        mongo.db.TCGA_lnc_relate.ensure_index("noncode_ID")
        mongo.db.cosmic_mut_in_lnc.ensure_index("lnc")
        mongo.db.target_gain.ensure_index("lncRNA")
        mongo.db.target_loss.ensure_index("lncRNA")
        mongo.db.tcga_target_gain.ensure_index("lncRNA")
        mongo.db.tcga_target_loss.ensure_index("lncRNA")
        mongo.db.cosmic_target_gain.ensure_index("lncRNA")
        mongo.db.cosmic_target_loss.ensure_index("lncRNA")
        mongo.db.human_target.ensure_index("lncRNA")
        mongo.db.human_target.ensure_index("conserve")
        mongo.db.human_target.ensure_index("expriment")
        mongo.db.human_target.ensure_index("expression")
        mongo.db.miRNA_expression.ensure_index("lnc")
        lnc_gene_list = list(mongo.db.lncRNA_gene_transcript.find(condition).skip(record_skip).limit(per_page))
        #test = list(mongo.db.lncRNA_gene_transcript.find().limit(10))
        combine_ls = []
        for var in lnc_gene_list:
            lnc = var['transcript']
            gain = mongo.db.target_gain.find({'lncRNA':lnc}).count()
            loss = mongo.db.target_loss.find({'lncRNA':lnc}).count()
            cons = mongo.db.human_target.find({"lncRNA":lnc,"conserve":1}).count()
            non_cons = mongo.db.human_target.find({"lncRNA":lnc,"conserve":0}).count()
            exp = mongo.db.human_target.find({"lncRNA":lnc,"experiment":1}).count()
            large = mongo.db.human_target.find({"lncRNA":lnc,"expression":{"$gte":1}}).count()
            small = mongo.db.human_target.find({"lncRNA": lnc, "expression": {"$lt": 1}}).count()
            tcga_count = mongo.db.TCGA_lnc_relate.find({"noncode_ID":lnc}).count()
            cosmic_count = mongo.db.cosmic_mut_in_lnc.find({"lnc":lnc}).count()
            tcga_gain = mongo.db.tcga_target_gain.find({"lncRNA":lnc}).count()
            tcga_loss = mongo.db.tcga_target_loss.find({"lncRNA":lnc}).count()
            cosmic_gain = mongo.db.cosmic_target_gain.find({"lncRNA": lnc}).count()
            cosmic_loss = mongo.db.cosmic_target_loss.find({"lncRNA": lnc}).count()
            var['tcga_count'] = tcga_count
            var['cosmic_count'] = cosmic_count
            var['tcga_gain'] = tcga_gain
            var['tcga_loss'] = tcga_loss
            var['cosmic_gain'] = cosmic_gain
            var['cosmic_loss'] = cosmic_loss
            var['cons'] = cons
            var['non_cons'] = non_cons
            var['large'] = large
            var['small'] = small
            var['exp'] = exp
            var['gain'] = gain
            var['loss'] = loss
            count = mongo.db.SNP_lnc_relate.find({'lnc':str(lnc)}).count()
            var['snp_count'] = count
            combine_ls.append(var)
        return {"lncrna_gene_list":combine_ls ,"records_number":records_number}
api.add_resource(LncGeneList, '/api/lncrna_gene_list')

class SnpBasicList(Resource):
    @marshal_with(snp_basic_list_fields)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int, default=1)
        parser.add_argument('per_page', type=int, default=15)
        parser.add_argument('snp')
        args = parser.parse_args()
        page = args['page']
        per_page = args['per_page']
        record_skip = (page - 1) * per_page
        condition = {}
        if args['snp']:
            condition = {"dbsnp": args['snp']}
        snp_basic_list = mongo.db.SNP_basic_info.find(condition).skip(record_skip).limit(per_page)
        return {'snp_basic_list': list(snp_basic_list)}
api.add_resource(SnpBasicList, '/api/snp_basic_list')

class miRNABasicList(Resource):
    @marshal_with(miR_basic_list_fields)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('page',type=int,default=1)
        parser.add_argument('per_page',type=int,default=15)
        parser.add_argument('mirna')
        parser.add_argument('single_tag')
        args = parser.parse_args()
        page = args['page']
        per_page = args['per_page']
        record_skip = (page-1)*per_page
        condition = {}
        mongo.db.miR_basic_info.ensure_index("miR_ID")
        mongo.db.miRNA_expression.ensure_index("miR")
        mongo.db.target_loss.ensure_index('miRNA')
        mongo.db.target_gain.ensure_index('miRNA')
        mongo.db.human_target.ensure_index('miRNA')
        mongo.db.human_target.ensure_index('conserve')
        combine_ls = []
        if args['mirna']:
            if not ',' in args['mirna']:
                condition = {'miR_ID':args['mirna']}
            else:
                mir_ls = args['mirna'].split(',')
                ls=[]
                for mir in mir_ls:
                    ls.append({'miR_ID':mir})
                condition = {"$or":ls}
        if not args['single_tag']:
            mir_exp = list(mongo.db.miR_basic_info.aggregate([{"$match":condition},{"$lookup":{"from":"miRNA_expression","localField":"miR_ID","foreignField":"miR","as":"exp_info"}},{"$unwind":"$exp_info"}]))
            for item in mir_exp:
                exp = item["exp_info"]
                item['expression'] = exp['expression']
                combine_ls.append(item)
        if args['single_tag']:
            mirna_info = mongo.db.miR_basic_info.find_one(condition)
            if mirna_info:
                mirna = mirna_info['miR_ID']
                gain = 0
                loss = 0
                cons = 0
                non_cons = 0
                if mongo.db.target_gain.find_one({'miRNA': mirna}).has_key('miRNA'):
                    gain = 1
                if mongo.db.target_loss.find_one({'miRNA': mirna}).has_key('miRNA'):
                    loss = 1
                if mongo.db.human_target.find_one({'miRNA': mirna,'conserve': 1}).has_key('miRNA'):
                    cons = 1
                if mongo.db.human_target.find_one({'miRNA': mirna,'conserve': 0}).has_key('miRNA'):
                    non_cons = 1
                mirna_info['gain'] = gain
                mirna_info['loss'] = loss
                mirna_info['cons'] = cons
                mirna_info['non_cons'] = non_cons
                exp = mongo.db.miRNA_expression.find_one({'miR':args['mirna']})
                mirna_info['expression'] = exp['expression']
                combine_ls.append(mirna_info)
        #miR_basic_list = mongo.db.miR_basic_info.find_one(condition)
        return {'miR_basic_list': combine_ls}
api.add_resource(miRNABasicList,'/api/miR_basic_list')

class miRNAExpressionList(Resource):
    @marshal_with(miR_exp_list_fields)
    def get(self):
        mongo.db.miRNA_expression.ensure_index("expression")
        hmirna_list = list(mongo.db.miRNA_expression.find({"expression": {"$gte":1000}}).sort([("id",1)])),
        mmirna_list = list(mongo.db.miRNA_expression.find({"expression": {"$lt": 1000,"$gte":10}}).sort([("id",1)])),
        lmirna_list = list(mongo.db.miRNA_expression.find({"expression": {"$lt": 10,"$gte":1}}).sort([("id",1)])),
        vmirna_list = list(mongo.db.miRNA_expression.find({"expression": {"$lte": 1}}).sort([("id",1)])),
        return {'hmirna_list': hmirna_list[0],'mmirna_list': mmirna_list[0],"lmirna_list":lmirna_list[0],'vmirna_list': vmirna_list[0]}

api.add_resource(miRNAExpressionList, '/api/mir_expression_list')

class miRNAProfileList(Resource):
    @marshal_with(miR_profile_list_fields)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int, default=1)
        parser.add_argument('per_page', type=int, default=15)
        parser.add_argument('mirna')
        args = parser.parse_args()
        page = args['page']
        per_page = args['per_page']
        record_skip = (page - 1) * per_page
        condition = {}
        if args['mirna']:
            condition['miR'] = args['mirna']
        mongo.db.miRNA_expression_sample.ensure_index("miR")
        mir_profile = mongo.db.miRNA_expression_sample.find(condition)
        return {'mirna_profile': list(mir_profile)}
api.add_resource(miRNAProfileList,'/api/mir_profile_list')

class TCGABasicList(Resource):
    @marshal_with(TCGA_basic_list_fields)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int, default=1)
        parser.add_argument('per_page', type=int, default=15)
        parser.add_argument('cancer')
        parser.add_argument('position')
        args = parser.parse_args()
        page = args['page']
        per_page = args['per_page']
        record_skip = (page - 1) * per_page
        condition = {}
        if args['cancer'] and args['position']:
            position = string.join(args['position'].split(';')[0:3],';')
            condition = {'cancer_type':args['cancer'],'mut_info':position}
        TCGA_basic_list = mongo.db.TCGA_basic_info.find_one(condition)
        mut_fre = mongo.db.cancer_fre.find_one({"mutation": position, "cancer": args['cancer']})
        chr_num, start, end = TCGA_basic_list["mut_info"].split(';')
        TCGA_basic_list['chromosome'] = str(chr_num)
        TCGA_basic_list["mut_start"] = int(start)
        TCGA_basic_list["mut_end"] = int(end)
        target_key = string.join(args['position'].split(';')[0:3],'_')+';'+string.join(args['position'].split(';')[3:5],';')
        gain = mongo.db.tcga_target_gain.find({"SNP": target_key}).count()
        loss = mongo.db.tcga_target_loss.find({"SNP": target_key}).count()
        TCGA_basic_list['gain'] = gain
        TCGA_basic_list['loss'] = loss
        TCGA_basic_list['target'] = gain+loss
        if mut_fre:
            TCGA_basic_list["fre"]=mut_fre['fre']
        else:
            TCGA_basic_list["fre"] = "-"
        return {'TCGA_basic_list': TCGA_basic_list}
api.add_resource(TCGABasicList,'/api/tcga_basic_list')

class TCGALncList(Resource):
    @marshal_with(TCGA_lnc_list_fields)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int, default=1)
        parser.add_argument('per_page', type=int, default=15)
        parser.add_argument('cancer',default="ACC")
        parser.add_argument('position')
        parser.add_argument('query')
        parser.add_argument('lncrna')
        args = parser.parse_args()
        page = args['page']
        per_page = args['per_page']
        record_skip = (page - 1) * per_page
        mongo.db.TCGA_lnc_relate.ensure_index("mut_info")
        mongo.db.TCGA_basic_info.ensure_index("mut_info")
        mongo.db.TCGA_mut_effect.ensure_index("Mut_info")
        mongo.db.tcga_target_gain.ensure_index("SNP")
        mongo.db.tcga_target_loss.ensure_index("SNP")
        mongo.db.lnrna_expression.ensure_index("lncrna")
        mongo.db.lncrNA_gene_transcript.ensure_index("transcipt")
        mongo.db.cancer_fre.ensure_index("mutation")
        mongo.db.cancer_fre.ensure_index("cancer")
        combine_ls = []
        condition={}
        cancer_ls = ["GBM","LUAD","BLCA","BRCA","CESC","COAD","HNSC","KICH","KIRC","KIRP","LGG","LIHC","LUSC","OV","PRAD","READ","SKCM","STAD","THCA","UCEC"]
        if args['position']:
            position = string.join(args['position'].split(';')[0:3], ';')
            condition = {'cancer_type': args['cancer'], 'mut_info': position}
        if args['cancer']:
            condition['cancer_type'] = args['cancer']
        if args['lncrna']:
            per_page=1000
            if "ENST" in args['lncrna']:
                noncode = mongo.db.noncode_esenmbl.find_one({"ensembl":args['lncrna']})
                lnc_name=noncode["noncode"]
            else:
                lnc_name=args['lncrna']
            condition={'noncode_ID':lnc_name}

        #tcga_lnc = mongo.db.TCGA_lnc_relate.aggregate([{"$match":condition},{"$lookup":{"from":"TCGA_mut_effect","localField":"mut_info","foreignField":"Mut_info","as":"info_detail"}},{"$unwind":"$info_detail"}])
        tcga_lnc = list(mongo.db.TCGA_lnc_relate.find(condition).sort([("chr",1),("noncode_ID",1)]).skip(record_skip).limit(per_page))
        if args['cancer'] and args['lncrna'] and args['query']:
            lnc_list = []
            if 'NONH' in args['lncrna']:
                condition = {"cancer_type":args['cancer'],'noncode_ID': {"$regex": args['lncrna'], "$options": "$i"}}
            else:
                condition_alia = {'alias': {"$regex": args['lncrna'], "$options": "$i"}}
                lncrna_info = list(mongo.db.NONCODE_alias.find(condition_alia))
                if len(lncrna_info)>1:
                    for item in lncrna_info:
                        lnc_list.append({'noncode_ID',item['transcript']})
                    condition = {"cancer_type":args['cancer'],'$or':lnc_list}
                if len(lncrna_info)==1:
                    condition = {"cancer_type": args['cancer'], 'noncode_ID': lncrna_info[0]['transcript']}
                else:
                    condition = {"cancer_type": args['cancer'], 'noncode_ID': args['lncrna']}
            # if "ENST" in args['lncrna']:
            #     noncode = mongo.db.noncode_esenmbl.find_one({"ensembl":args['lncrna']})
            #     lnc_name=noncode["noncode"]
            # else:
            #     lnc_name=args['lncrna']
            # condition ={"cancer_type":args['cancer'],'noncode_ID':lnc_name}
            tcga_lnc = list( mongo.db.TCGA_lnc_relate.find(condition))
        tanric=0
        for item in tcga_lnc:
            lnc = item["noncode_ID"]
            mutation = item["mut_info"]
            gene_ls = list(mongo.db.lncRNA_gene_transcript.find({"transcript":str(lnc)}))
            gene = gene_ls[0]["gene"]
            express = 0
            tanric = 0
            effect = 0
            mut_fre = mongo.db.cancer_fre.find_one({"mutation":mutation,"cancer":item['cancer_type']})
            home_lnc_search_express=0
            if args['cancer'] in cancer_ls:
                tanric = 1
            if args['cancer'] in cancer_ls and mongo.db.lncrna_expression.find({"lncrna":str(gene)}).count()!=0:
                express = 1
            if mongo.db.lncrna_expression.find({"lncrna":str(gene)}).count()!=0:
                home_lnc_search_express=1
            item["home_lnc_search_express"] = home_lnc_search_express
            item["express"] = express
            pos = item["mut_info"]
            effect_info = mongo.db.TCGA_mut_effect.find_one({"Mut_info":str(pos)})
            if effect_info:
                effect = 1
                item["noncoding_group"]=effect_info["Noncoding_Groups"]
                item["noncoding_score"]=effect_info["Noncoding_Score"]
            item["effect"] = effect
            cancer=item['cancer_type']
            detail = mongo.db.TCGA_basic_info.find_one({"cancer_type":cancer,"mut_info":str(pos)})
            chr_num, start, end = item["mut_info"].split(';')
            item["mut_start"] = int(start)
            item["mut_end"] = int(end)
            if mut_fre:
                item["fre"] = mut_fre['fre']
            else:
                item["fre"] = "-"
            item["ref_base"] = detail["Tumor_Seq_Allele1"]
            item["alt_base"] = detail["Tumor_Seq_Allele2"]
            target_key = string.join(pos.split(';'),'_')+';'+detail["Tumor_Seq_Allele1"]+';'+detail["Tumor_Seq_Allele2"]
            gain = mongo.db.tcga_target_gain.find({"SNP":target_key}).count()
            loss = mongo.db.tcga_target_loss.find({"SNP":target_key}).count()
            item['gain'] = gain
            item['loss'] = loss
            item['target'] = gain+loss
            combine_ls.append(item)
        number = mongo.db.TCGA_lnc_relate.find(condition).count()
        return {'TCGA_lnc_list':combine_ls,"records_number":number,"tanric":tanric}
api.add_resource(TCGALncList,'/api/tcga_lnc_list')

class TCGAMutEffectList(Resource):
    @marshal_with(TCGA_mut_effect_list_fields)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int, default=1)
        parser.add_argument('per_page', type=int, default=15)
        parser.add_argument('cancer')
        args = parser.parse_args()
        page = args['page']
        per_page = args['per_page']
        record_skip = (page - 1) * per_page
        condition = {}
        if args['cancer']:
            condition = {'cancer_type': args['cancer']}
        TCGA_mut_effect_list = mongo.db.TCGA_mut_effect.find(condition).skip(record_skip).limit(per_page)
        return {'TCGA_mut_effect_list':list(TCGA_mut_effect_list)}
api.add_resource(TCGAMutEffectList,'/api/tcga_mut_effect_list')

class GWASBasicList(Resource):
    @marshal_with(gwas_basic_list_fields)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int, default=1)
        parser.add_argument('per_page', type=int, default=15)
        parser.add_argument('snp')
        args = parser.parse_args()
        page = args['page']
        per_page = args['per_page']
        record_skip = (page - 1) * per_page
        snp=''
        gwas_basic_list = []
        tag_snp_list = []
        if args['snp']:
            tag_snp_list = list(mongo.db.snp_tagSNP_pair.find({"dbsnp": args['snp']}))
        for var in tag_snp_list:
            tagSNP = var['tagSNP']
            temp_list = list(mongo.db.gwas_basic_info.find({"SNPS":tagSNP}))
            gwas_basic_list.append(temp_list[0])
        return {'gwas_basic_list':list(gwas_basic_list)}
api.add_resource(GWASBasicList,'/api/gwas_basic_list')

class GwasLDList(Resource):
    @marshal_with(gwas_ld_list_fields)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int, default=1)
        parser.add_argument('per_page', type=int, default=15)
        parser.add_argument('snp')
        args = parser.parse_args()
        page = args['page']
        per_page = args['per_page']
        record_skip = (page - 1) * per_page
        condition = {}
        ld_list = []
        tag_snp_list = []
        tagsnp_list = list(mongo.db.snp_tagSNP_common.find().sort([("tagSNP",1)]))
        if args['snp']:
            condition['dbsnp'] = args['snp']
        tag_snp_list = list(mongo.db.snp_tagSNP_pair.find(condition).limit(per_page))
        #gwas_info = list(mongo.db.gwas_ld_snp.aggregate([{"$lookup": {"from": "SNP_lnc_relate", "localField": "tagSNP", "foreignField": "tagSNP", "as": "info_detail"}}]))
        for var in tag_snp_list:
            tagSNP = var['tagSNP']
            gwas_info = list(mongo.db.gwas_ld_snp.find({'tagSNP':tagSNP}).sort([("tagSNP",1)]))
            for info in gwas_info:
                if "CEU_REGION" in info:
                    chr_num,ceu_start,ceu_end = info["CEU_REGION"].split(',')
                    info["CEU_start"] = str(ceu_start)
                    info["CEU_end"] = str(ceu_end)
                if "YRI_REGION" in info:
                    chr_num,yri_start,yri_end = info["YRI_REGION"].split(',')
                    info["YRI_start"] = str(yri_start)
                    info["YRI_end"] = str(yri_end)
                if "ASW_REGION" in info:
                    chr_num,asw_start,asw_end = info["ASW_REGION"].split(',')
                    info["ASW_start"] = str(asw_start)
                    info["ASW_end"] = str(asw_end)
                if "CHD_REGION" in info:
                    chr_num,chd_start,chd_end = info["CHD_REGION"].split(',')
                    info["CHD_start"] = str(chd_start)
                    info["CHD_end"] = str(chd_end)
                if "GIH_REGION" in info:
                    chr_num,gih_start,gih_end = info["GIH_REGION"].split(',')
                    info["GIH_start"] = str(gih_start)
                    info["GIH_end"] = str(gih_end)
                if "LWK_REGION" in info:
                    chr_num,lwk_start,lwk_end = info["LWK_REGION"].split(',')
                    info["LWK_start"] = str(lwk_start)
                    info["LWK_end"] = str(lwk_end)
                if "MEX_REGION" in info:
                    chr_num,mex_start,mex_end = info["MEX_REGION"].split(',')
                    info["MEX_start"] = str(mex_start)
                    info["MEX_end"] = str(mex_end)
                if "MKK_REGION" in info:
                    chr_num,mkk_start,mkk_end = info["MKK_REGION"].split(',')
                    info["MKK_start"] = str(mkk_start)
                    info["MKK_end"] = str(mkk_end)
                if "TSI_REGION" in info:
                    chr_num,tsi_start,tsi_end = info["TSI_REGION"].split(',')
                    info["TSI_start"] = str(tsi_start)
                    info["TSI_end"] = str(tsi_end)
            ld_list.append(info)
        return {'gwas_ld_list':ld_list,'tagSNP_list':tagsnp_list}
api.add_resource(GwasLDList,'/api/gwas_ld_list')

class CosmicBasicList(Resource):
    @marshal_with(cosmic_basic_list_fields)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int, default=1)
        parser.add_argument('per_page', type=int, default=15)
        parser.add_argument('lncrna')
        args = parser.parse_args()
        page = args['page']
        per_page = args['per_page']
        record_skip = (page - 1) * per_page
        condition = {}
        mongo.db.cosmic_basic_info.ensure_index("genome position")
        mongo.db.cosmic_mut_in_lnc.ensure_index("mut_info")
        combine_info = list(mongo.db.cosmic_mut_in_lnc.aggregate([{"$match":condition},{"$lookup":{
            "from": "cosmic_basic_info", "localField": "mut_info", "foreignField": "genome position", "as": "info_detail"}},
                                                                  {"$unwind": "$info_detail"}, {"$skip": record_skip}, {"$limit": per_page}]))
        info_all = []
        for temp in combine_info:
            info = temp["info_detail"]
            target_key = temp["ID_NCV"]
            gain = mongo.db.cosmic_target_gain.find({"SNP": target_key}).count()
            loss = mongo.db.cosmic_target_loss.find({"SNP": target_key}).count()
            temp['gain'] = gain
            temp['loss'] = loss
            temp['target'] = gain+loss
            for key in info:
                temp[key] = info[key]
            info_all.append(temp)
        return {'cosmic_basic_list': info_all}
api.add_resource(CosmicBasicList, '/api/cosmic_basic_list')

class CosmicLncList(Resource):
    @marshal_with(cosmic_lnc_list_fields)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int, default=1)
        parser.add_argument('per_page', type=int, default=15)
        parser.add_argument('ncv_id')
        parser.add_argument('lncrna')
        parser.add_argument('chr')
        args = parser.parse_args()
        page = args['page']
        per_page = args['per_page']
        record_skip = (page - 1) * per_page
        condition = {}
        if args['ncv_id']:
            condition = {'CNV_ID': args['ncv_id']}
        if args['lncrna']:
            per_page=1000
            if "ENST" in args['lncrna']:
                noncode = mongo.db.noncode_esenmbl.find_one({"ensembl": args['lncrna']})
                lnc_name = noncode["noncode"]
            else:
                lnc_name = args['lncrna']
            condition["lnc"] = lnc_name
        if args['chr']:
            condition['chr'] = args['chr']
        mongo.db.cosmic_mut_in_lnc.ensure_index("CNV_ID")
        mongo.db.cosmic_mut_in_lnc.ensure_index("chr")
        mongo.db.cosmic_basic_info.ensure_index("ID_NCV")
        mongo.db.cosmic_mut_in_lnc.ensure_index("lnc")
        mongo.db.cosmic_target_gain.ensure_index("SNP")
        mongo.db.cosmic_target_loss.ensure_index("SNP")
        records_number = mongo.db.cosmic_mut_in_lnc.find(condition).count()
        #cosmic_lnc_list = list(mongo.db.cosmic_mut_in_lnc.find(condition).skip(record_skip).limit(per_page))
        combine_info = list(mongo.db.cosmic_mut_in_lnc.aggregate([{"$match": condition}, {"$lookup": {
            "from": "cosmic_basic_info", "localField": "CNV_ID", "foreignField": "ID_NCV",
            "as": "info_detail"}}, {"$unwind": "$info_detail"}, {"$skip": record_skip}, {"$limit": per_page}]))
        info_all = []
        for temp in combine_info:
            info = temp["info_detail"]
            position = info["genome position"]
            chr,start,end = position.split(';')
            temp["mut_start"] = start
            temp["mut_end"] = end
            temp["WT_SEQ"] = info["WT_SEQ"]
            temp["MUT_SEQ"] = info["MUT_SEQ"]
            if "FATHMM_MKL_NON_CODING_GROUPS" in info:
                temp["FATHMM_MKL_NON_CODING_GROUPS"] = info["FATHMM_MKL_NON_CODING_GROUPS"]
            if "FATHMM_MKL_NON_CODING_SCORE" in info:
                temp["FATHMM_MKL_NON_CODING_SCORE"] = info["FATHMM_MKL_NON_CODING_SCORE"]
            target_key = temp["CNV_ID"]+';'+info["WT_SEQ"]+';'+info["MUT_SEQ"]
            gain = mongo.db.cosmic_target_gain.find({"SNP": target_key}).count()
            loss = mongo.db.tcga_target_loss.find({"SNP": target_key}).count()
            temp['gain'] = gain
            temp['loss'] = loss
            temp['target'] = gain + loss
            info_all.append(temp)
        return {'cosmic_lnc_list': info_all,'records_number':records_number}

api.add_resource(CosmicLncList, '/api/cosmic_lnc_list')

class LncRNASNPList(Resource):
    @marshal_with(lncrna_snp_list_fields)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int,default=1)
        parser.add_argument('per_page', type=int,default=15)
        parser.add_argument('lncrna')
        parser.add_argument('snp')
        parser.add_argument('ld')
        parser.add_argument('gmaf')
        parser.add_argument('effect')
        parser.add_argument('target')
        parser.add_argument('exp')
        parser.add_argument('chr')
        parser.add_argument('start')
        parser.add_argument('end')
        args = parser.parse_args()
        page = args['page']
        per_page = args['per_page']
        record_skip = (page-1) * per_page
        condition = {}
        if args['chr']:
            condition["chr"] = args['chr']
        if args['lncrna']:
            if not ',' in args['lncrna']:
                if "ENST" in args['lncrna']:
                    noncode = mongo.db.noncode_esenmbl.find_one({"ensembl":args['lncrna']})
                    lnc_name=noncode["noncode"]
                else:
                    lnc_name=args['lncrna']
                condition["lnc"] = lnc_name
            else:
                lncrna_ls = args['lncrna'].split(',')
                ls = []
                for lncrna in lncrna_ls:
                    ls.append({"lnc": lncrna})
                condition = {"$or": ls}
        if args['snp']:
            if not ',' in args['snp']:
                condition["dbsnp"] = args['snp']
            else:
                snp_ls = args['snp'].split(',')
                ls=[]
                for snp in snp_ls:
                    ls.append({"dbsnp":snp})
                condition={"$or":ls}
        if args['start']:
            condition["start"] = {"$gt":int(args['start'])}
        if args['end']:
            condition["end"] = {"$lt":int(args['end'])}
        if args['gmaf']:
            condition["a_fre"] = {"$gt":float(args['gmaf'][1:])}
        if args['ld']:
            condition['ld'] = int(args['ld'])
        if args['target']:
            condition['impact'] = int(args['target'])
        if args['exp']:
            condition['experiment'] = int(args['exp'])
        if args['effect']:
            condition['structure'] = int(args['effect'])
        print condition
        mongo.db.SNP_basic_info.ensure_index("dbsnp")
        mongo.db.SNP_basic_info.ensure_index("alt_base")
        mongo.db.SNP_lnc_relate.ensure_index("dbsnp")
        mongo.db.SNP_lnc_relate.ensure_index("chr")
        mongo.db.SNP_lnc_relate.ensure_index("start")
        mongo.db.SNP_lnc_relate.ensure_index("a_fre")
        mongo.db.SNP_lnc_relate.ensure_index("experiment")
        mongo.db.SNP_lnc_relate.ensure_index("structure")
        mongo.db.SNP_lnc_relate.ensure_index("impact")
        mongo.db.SNP_lnc_relate.ensure_index("ld")
        mongo.db.SNP_lnc_relate.ensure_index("start")
        mongo.db.SNP_lnc_relate.ensure_index("end")
        mongo.db.SNP_lnc_relate.ensure_index("lnc")
        mongo.db.snp_tagSNP_pair.ensure_index("dbsnp")
        mongo.db.snp_tagSNP_common.ensure_index("dbSNP")
        mongo.db.target_gain.ensure_index("snp")
        mongo.db.target_loss.ensure_index("snp")
        mongo.db.rnasnp_data.ensure_index("dbSNP")
        mongo.db.rnasnp_data.ensure_index("lnc")
        if condition=={}:
            lncrna_snp_list = mongo.db.SNP_lnc_relate.find(condition).skip(record_skip).limit(per_page)
        else:
            lncrna_snp_list = mongo.db.SNP_lnc_relate.find(condition)
        records_number= mongo.db.SNP_lnc_relate.find(condition).count()
        combine_ls=[]
        for item in lncrna_snp_list:
            tagsnp = 0
            snp_tagsnp = 0
            target = 0
            gain = 0
            loss = 0
            effect=0
            snp = item["dbsnp"]
            lncrna = item["lnc"]
            gene_ls = list(mongo.db.lncRNA_gene_transcript.find({"transcript": lncrna}))
            gene = gene_ls[0]["gene"]
            express = mongo.db.lncrna_expression.find({"lncrna": str(gene)}).count()
            if mongo.db.rnasnp_data.find({'dbSNP':snp}).count()>0:
                effect=1
            if mongo.db.snp_tagSNP_common.find({'dbsnp': snp}).count() > 0:
                snp_tagsnp = 1
            item['effect'] = effect
            item['express'] = express
            item['snp_tagSNP'] = snp_tagsnp
            snp_info = mongo.db.SNP_basic_info.find_one({"dbsnp":snp})
            item["pos"] = snp_info["pos"]
            item["a_base"] = snp_info["alt_base"]
            if mongo.db.target_gain.find({"SNP":snp}).count() > 0:
                target = 1
                gain = 1
            if mongo.db.target_loss.find({"SNP":snp}).count() > 0:
                target = 1
                loss = 1
            effect_data = mongo.db.rnasnp_data.find_one({"dbSNP": snp})
            if effect_data:
                effect = 1
                data=effect_data
                item["GC"] = data["GC"]
                item["p1"] = data["p-value_1"]
                item["p2"] = data["p-value_2"]
                item["d_max"] = data["d_max"]
                item["r_min"] = data["r_min"]
                item["interval_1"] = data["interval_1"]
                item["interval_2"] = data["interval_2"]
            item['target'] = target
            item['gain'] = gain
            item['loss'] = loss
            item['effect'] = effect
            combine_ls.append(item)
        return {'lncrna_snp_list': combine_ls, 'records_number': records_number}
        #return {'lncrna_snp_list':list(lncrna_snp_list),'records_number':records_number}

api.add_resource(LncRNASNPList, '/api/lncrna_snp_list')






