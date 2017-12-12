@app.route("/browseGeneNetwork")
def browseGeneNetwork():
    dataSource = request.args.get("source")
    input_gene = request.args.get('gene')
    input_tissue = request.args.get('tissue')
    input_tissue = input_tissue.encode('gb2312').split('; ')
    curs = mysql.connection.cursor()
    # print dataSource
    # print input_tissue
    # print input_gene
    total_list = []
    if dataSource == "TCGA":
        for i in input_tissue:
            # print i
            sql = '''SELECT id,cancer,gene,tag,miR,gene_TF,TF_target FROM TCGA WHERE cancer="%s" and gene="%s"''' % (i, input_gene)
            # print sql
            curs.execute(sql)
            result = curs.fetchall()
            da = list(result)

            total_list.append(da)
    if dataSource == "EBI":
        for i in input_tissue:
            # print i
            sql = '''SELECT id,tissue,gene,tag,miR,gene_TF,TF_target FROM EBI WHERE tissue="%s" and gene="%s"''' % (i, input_gene)
            # print sql
            curs.execute(sql)
            result = curs.fetchall()
            da = list(result)
            total_list.append(da)
    if dataSource == "CCLE":
        for i in input_tissue:
            # print i
            sql = '''SELECT id,tissue,gene,tag,miR,gene_TF,TF_target FROM TCGA WHERE tissue="%s" and gene="%s"''' % (i, input_gene)
            # print sql
            curs.execute(sql)
            result = curs.fetchall()
            da = list(result)

            total_list.append(da)
    if dataSource == "GTEx":
        for i in input_tissue:
            # print i
            sql = '''SELECT id,tissue,gene,tag,miR,gene_TF,TF_target FROM TCGA WHERE tissue="%s" and gene="%s"''' % (i, input_gene)
            # print sql
            curs.execute(sql)
            result = curs.fetchall()
            da = list(result)
            total_list.append(da)
    tissue = []
    total_list2=[]
    for genes in total_list:
        params_miR = []
        input_gene_TF = []
        params_TF_gene = []
        print genes[0][1]
        tissue.append(genes[0][1])

        # print genes
        for i in genes:
            # tissue.add(i[1])
            input_gene_TF.extend(i[5].split('; '))
            params_TF_gene.extend(i[6].split('; '))
            miRNA = i[4].split("; ")
            for j in miRNA:
                j = j.strip().split(":")[0]
                params_miR.append(j)
        if params_miR[0] != '-' and input_gene_TF[0] != '-' and params_TF_gene[0] != '-':
            seg_node = []
            seg_edge = []
            seg_attr = []
            seg_node.append('\\<graphml>\\<key id="label" for="all" attr.name="label" attr.type="string"/>\\<key id="weight" for="node" attr.name="weight" attr.type="double"/>\\<graph edgedefault="directed">')
            node1 = '\\<node id = "-1"><data key = "label">' + input_gene + '</data></node>'
            seg_node.append(node1)
            n = 0
            m = 1000
            o = 10000
            for j in params_miR:
                j = j.strip()
                node2 = '\\<node id="' + str(n) + '"><data key="label">' + j + '</data></node>'
                edge2 = '\\<edge source="' + str(n) + '" target="-1"></edge>'
                attr2 = '{ attrValue: ' + str(n) + ', value: "#50b7c1" },'
                seg_node.append(node2)
                seg_edge.append(edge2)
                seg_attr.append(attr2)
                n += 1
            for i in input_gene_TF:
                i = i.strip()
                node3 = '\\<node id="' + str(m) + '"><data key="label">' + i + '</data></node>'
                edge3 = '\\<edge source="' + str(m) + '" target="-1"></edge>'
                attr3 = '{ attrValue: ' + str(m) + ', value: "#B23AEE" },'
                seg_node.append(node3)
                seg_edge.append(edge3)
                seg_attr.append(attr3)
                m += 1
            for i in params_TF_gene:
                i = i.strip()
                node4 = '\\<node id="' + str(o) + '"><data key="label">' + i + '</data></node>'
                edge4 = '\\<edge source="-1" ' + 'target="' + str(o) + '"></edge>'
                attr4 = '{ attrValue: ' + str(o) + ', value: "#9ACD32" },'
                seg_node.append(node4)
                seg_edge.append(edge4)
                seg_attr.append(attr4)
                o += 1
            seg_edge.append('\\           </graph>' + '\\' + '\n' + '</graphml>\\')
            totaldata = ''.join(seg_node) + ''.join(seg_edge)
            totalattr = ''.join(seg_attr)
            # return render_template("allDBnetwork.html", total_data=totaldata, total_attr=totalattr, genename=str(input_gene),dataSource=str(dataSource), input_tissue=str(input_tissue))
    # total_list2.append((totaldata,totalattr,genename,dataSource,input_tissue))
        if params_miR[0] == '-' and input_gene_TF[0] != '-' and params_TF_gene[0] != '-':
            seg_node = []
            seg_edge = []
            seg_attr = []
            seg_node.append('\\<graphml>\\<key id="label" for="all" attr.name="label" attr.type="string"/>\\<key id="weight" for="node" attr.name="weight" attr.type="double"/>\\<graph edgedefault="directed">')
            node1 = '\\<node id = "-1"><data key = "label">' + input_gene + '</data></node>'
            seg_node.append(node1)
            m = 1000
            o = 10000
            for i in input_gene_TF:
                i = i.strip()
                node3 = '\\<node id="' + str(m) + '"><data key="label">' + i + '</data></node>'
                edge3 = '\\<edge source="' + str(m) + '" target="-1"></edge>'
                attr3 = '{ attrValue: ' + str(m) + ', value: "#B23AEE" },'
                seg_node.append(node3)
                seg_edge.append(edge3)
                seg_attr.append(attr3)
                m += 1
            for i in params_TF_gene:
                i = i.strip()
                node4 = '\\<node id="' + str(o) + '"><data key="label">' + i + '</data></node>'
                edge4 = '\\<edge source="-1" ' + 'target="' + str(o) + '"></edge>'
                attr4 = '{ attrValue: ' + str(o) + ', value: "#9ACD32" },'
                seg_node.append(node4)
                seg_edge.append(edge4)
                seg_attr.append(attr4)
                o += 1
            seg_edge.append('\\           </graph>' + '\\' + '\n' + '</graphml>\\')
            totaldata = ''.join(seg_node) + ''.join(seg_edge)
            totalattr = ''.join(seg_attr)
            # return render_template("allDBnetwork.html", total_data=totaldata, total_attr=totalattr, genename=str(input_gene),dataSource=str(dataSource), input_tissue=str(input_tissue))
        # total_list2.append((totaldata, totalattr, genename, dataSource, input_tissue))
        if params_miR[0] != '-' and input_gene_TF[0] != '-' and params_TF_gene[0] == '-':
            seg_node = []
            seg_edge = []
            seg_attr = []
            seg_node.append('\\<graphml>\\<key id="label" for="all" attr.name="label" attr.type="string"/>\\<key id="weight" for="node" attr.name="weight" attr.type="double"/>\\<graph edgedefault="directed">')
            node1 = '\\<node id = "-1"><data key = "label">' + input_gene + '</data></node>'
            seg_node.append(node1)
            n = 0
            m = 1000
            for j in params_miR:
                j = j.strip()
                node2 = '\\<node id="' + str(n) + '"><data key="label">' + j + '</data></node>'
                edge2 = '\\<edge source="' + str(n) + '" target="-1"></edge>'
                attr2 = '{ attrValue: ' + str(n) + ', value: "#50b7c1" },'
                seg_node.append(node2)
                seg_edge.append(edge2)
                seg_attr.append(attr2)
                n += 1
            for i in input_gene_TF:
                i = i.strip()
                node3 = '\\<node id="' + str(m) + '"><data key="label">' + i + '</data></node>'
                edge3 = '\\<edge source="' + str(m) + '" target="-1"></edge>'
                attr3 = '{ attrValue: ' + str(m) + ', value: "#B23AEE" },'
                seg_node.append(node3)
                seg_edge.append(edge3)
                seg_attr.append(attr3)
                m += 1
            seg_edge.append('\\           </graph>' + '\\' + '\n' + '</graphml>\\')
            totaldata = ''.join(seg_node) + ''.join(seg_edge)
            totalattr = ''.join(seg_attr)
            # print totaldata
            # print totalattr
            # return render_template("allDBnetwork.html", total_data=totaldata, total_attr=totalattr, genename=str(input_gene), dataSource=str(dataSource), input_tissue=str(input_tissue))
        # total_list2.append((totaldata, totalattr, genename, dataSource, input_tissue))
        if params_miR[0] == '-' and input_gene_TF[0] != '-' and params_TF_gene[0] == '-':
            seg_node = []
            seg_edge = []
            seg_attr = []
            seg_node.append('\\<graphml>\\<key id="label" for="all" attr.name="label" attr.type="string"/>\\<key id="weight" for="node" attr.name="weight" attr.type="double"/>\\<graph edgedefault="directed">')
            node1 = '\\<node id = "-1"><data key = "label">' + input_gene + '</data></node>'
            seg_node.append(node1)
            m = 1000
            for i in input_gene_TF:
                i = i.strip()
                node3 = '\\<node id="' + str(m) + '"><data key="label">' + i + '</data></node>'
                edge3 = '\\<edge source="' + str(m) + '" target="-1"></edge>'
                attr3 = '{ attrValue: ' + str(m) + ', value: "#B23AEE" },'
                seg_node.append(node3)
                seg_edge.append(edge3)
                seg_attr.append(attr3)
                m += 1
            seg_edge.append('\\           </graph>' + '\\' + '\n' + '</graphml>\\')
            totaldata = ''.join(seg_node) + ''.join(seg_edge)
            totalattr = ''.join(seg_attr)
            # print totaldata
            # print totalattr
            # return render_template("allDBnetwork.html", total_data=totaldata, total_attr=totalattr, genename=str(input_gene), dataSource=str(dataSource), input_tissue=str(input_tissue))
        # total_list2.append((totaldata, totalattr, genename, dataSource, input_tissue))
        if params_miR[0] != '-' and input_gene_TF[0] == '-' and params_TF_gene[0] != '-':
            seg_node = []
            seg_edge = []
            seg_attr = []
            seg_node.append('\\<graphml>\\<key id="label" for="all" attr.name="label" attr.type="string"/>\\<key id="weight" for="node" attr.name="weight" attr.type="double"/>\\<graph edgedefault="directed">')
            node1 = '\\<node id = "-1"><data key = "label">' + input_gene + '</data></node>'
            seg_node.append(node1)
            n = 0
            for j in params_miR:
                j = j.strip()
                node2 = '\\<node id="' + str(n) + '"><data key="label">' + j + '</data></node>'
                edge2 = '\\<edge source="' + str(n) + '" target="-1"></edge>'
                attr2 = '{ attrValue: ' + str(n) + ', value: "#50b7c1" },'
                seg_node.append(node2)
                seg_edge.append(edge2)
                seg_attr.append(attr2)
                n += 1
            m = 1000
            for i in params_TF_gene:
                i = i.strip()
                node3 = '\\<node id="' + str(m) + '"><data key="label">' + i + '</data></node>'
                # edge3 = '\\<edge source="' + str(m) + '" target="-1"></edge>'
                edge3 = '\\<edge source="-1" ' + 'target="' + str(m) + '"></edge>'
                attr3 = '{ attrValue: ' + str(m) + ', value: "#B23AEE" },'
                seg_node.append(node3)
                seg_edge.append(edge3)
                seg_attr.append(attr3)
                m += 1
            seg_edge.append('\\           </graph>' + '\\' + '\n' + '</graphml>\\')
            totaldata = ''.join(seg_node) + ''.join(seg_edge)
            totalattr = ''.join(seg_attr)
            # print totaldata
            # print totalattr
            # return render_template("allDBnetwork.html", total_data=totaldata, total_attr=totalattr, genename=str(input_gene),dataSource=str(dataSource), input_tissue=str(input_tissue))
        # total_list2.append((totaldata, totalattr, genename, dataSource, input_tissue))
        if params_miR[0] == '-' and input_gene_TF[0] == '-' and params_TF_gene[0] != '-':
            seg_node = []
            seg_edge = []
            seg_attr = []
            seg_node.append('\\<graphml>\\<key id="label" for="all" attr.name="label" attr.type="string"/>\\<key id="weight" for="node" attr.name="weight" attr.type="double"/>\\<graph edgedefault="directed">')
            node1 = '\\<node id = "-1"><data key = "label">' + input_gene + '</data></node>'
            seg_node.append(node1)
            m = 1000
            for i in params_TF_gene:
                i = i.strip()
                node3 = '\\<node id="' + str(m) + '"><data key="label">' + i + '</data></node>'
                # edge3 = '\\<edge source="' + str(m) + '" target="-1"></edge>'
                edge3 = '\\<edge source="-1" ' + 'target="' + str(m) + '"></edge>'
                attr3 = '{ attrValue: ' + str(m) + ', value: "#B23AEE" },'
                seg_node.append(node3)
                seg_edge.append(edge3)
                seg_attr.append(attr3)
                m += 1
            seg_edge.append('\\           </graph>' + '\\' + '\n' + '</graphml>\\')
            totaldata = ''.join(seg_node) + ''.join(seg_edge)
            totalattr = ''.join(seg_attr)
            # return render_template("allDBnetwork.html", total_data=totaldata, total_attr=totalattr, genename=str(input_gene),dataSource=str(dataSource), input_tissue=str(input_tissue))
        # total_list2.append((totaldata, totalattr, genename, dataSource, input_tissue))
        if params_miR[0] != '-' and input_gene_TF[0] == '-' and params_TF_gene[0] == '-':
            seg_node = []
            seg_edge = []
            seg_attr = []
            seg_node.append('\\<graphml>\\<key id="label" for="all" attr.name="label" attr.type="string"/>\\<key id="weight" for="node" attr.name="weight" attr.type="double"/>\\<graph edgedefault="directed">')
            node1 = '\\<node id = "-1"><data key = "label">' + input_gene + '</data></node>'
            seg_node.append(node1)
            m = 1000
            for i in params_miR:
                i = i.strip()
                node3 = '\\<node id="' + str(m) + '"><data key="label">' + i + '</data></node>'
                edge3 = '\\<edge source="' + str(m) + '" target="-1"></edge>'
                attr3 = '{ attrValue: ' + str(m) + ', value: "#B23AEE" },'
                seg_node.append(node3)
                seg_edge.append(edge3)
                seg_attr.append(attr3)
                m += 1
            seg_edge.append('\\           </graph>' + '\\' + '\n' + '</graphml>\\')
            totaldata = ''.join(seg_node) + ''.join(seg_edge)
            totalattr = ''.join(seg_attr)
            # print totaldata
            # print totalattr
            # return render_template("allDBnetwork.html", total_data=totaldata, total_attr=totalattr, genename=str(input_gene),dataSource=str(dataSource), input_tissue=str(input_tissue))
        # total_list2.append((totaldata, totalattr, genename, dataSource, input_tissue))
        if params_miR[0] == '-' and input_gene_TF[0] == '-'and params_TF_gene[0] == '-':
            totaldata = ''
            totalattr = ''
        total_list2.append((totaldata, totalattr))
    print len(total_list2)
    genename = str(input_gene)
    dataSource = str(dataSource)
    input_tissue = tissue
    seg=[]
    nn=1
    mm=0
    for li in total_list2:
        # print li
        totaldata, totalattr = li
        if totaldata and totalattr:
            code='''<h3>Regulatory network of %s gene in %s %s</h3>
                    <div id="%sa" style="width:1200px;height:800px;"></div>
                    <script type="text/javascript">
                    var xml = '%s
                    ';
                    var visual_style = {
                        nodes: {
                                    borderColor: "#FFFFFF",
                                    borderWidth: 0,
                                    size: 40,
                                    color: {
                                        discreteMapper: {
                                            attrName: "id",
                                            entries: [
                                                { attrValue: -1, value: "#EEEE00" },
                                                %s
                                               ]
                                        }
                                    },
                                    labelHorizontalAnchor: "center",
                                    labelFontSize: 16,
                                    labelFontColor: "#000000",
                                    labelFontWeight: "bold"
                                }
                    }
                var options = { swfPath: "/static/SEG/cytoscape/swf/CytoscapeWeb"}
                var vis = new org.cytoscapeweb.Visualization("%sa",options);
                vis.draw({ network: xml, visualStyle: visual_style });
                </script><br/>''' %(genename,dataSource,input_tissue[mm],nn,totaldata,totalattr,nn)
            nn += 1
            mm+=1
            # print code
            seg.append(code)
        else:
            code='''<h3>Regulatory network of %s gene in %s %s </h3>
                    <div id="%sa" style="width:1200px;height:200px;"><h3 align="center" style="color:blue">No regulatory data found.</h3></div>''' % (genename,dataSource,input_tissue[mm],nn)
            nn += 1
            mm += 1
            seg.append(code)
    print '<br/>'.join(seg)
    return render_template("genenetwork.html", code='<br/>'.join(seg))
