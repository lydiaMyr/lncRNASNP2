'use strict';
angular.module('lncRNASNP2')
    .controller('TcgaMutationDetailController', TcgaMutationDetailController);
function TcgaMutationDetailController($scope,$http,$routeParams,lncRNASNP2Service) {
    var base_url = lncRNASNP2Service.getAPIBaseUrl();
    $("[data-toggle='popover']").popover();
    $scope.wrong=0;
    $scope.clear = function () {
        $scope.one=0;
        $scope.two=0;
        $scope.three=0;
        $scope.four=0;
        $scope.five=0;
    };
    $scope.one=1;
    var flag=0;
    $scope.show_one = function (refer) {
        $scope.clear();
        if (refer=="one"){
            $scope.one=1;
            $scope.class_one ="active"
        }
        if (refer=="two"){
            $scope.two=1;
            $scope.class_two ="active"
        }
        if (refer=="three"){
            $scope.three=1;
            $scope.class_three ="active"
        }
        if (refer=="four"){
            $scope.four=1;
            $scope.class_four ="active"
        }
        if (refer=="five"){
            $scope.five=1;
            $scope.class_five ="active"
        }
    };
    $scope.modal_title = function (item) {
        $scope.modal_header = "Target Gain";
        $scope.target = item;
    };
    $scope.modal_title1 = function (item) {
        $scope.modal_header = "Target Loss";
        $scope.target = item;
    };
     $scope.check = function (query_item) {
        if(/[@#\$%\^&\*]+/g.test(query_item)){
            flag=1;
            alert("Invalid input");
            history.back();
        }
    };

    $scope.fetch_target_gain = function () {
        $http({
            url: base_url+'/api/tcga_target_gain_list',
            params: {snp:$routeParams.position},
            method: 'GET'
        }).then(
            function(response){
                $scope.target_gain = response.data.target_gain_list
            }
        )
    };
    $scope.fetch_target_loss = function () {
        $http({
            url: base_url+'/api/tcga_target_loss_list',
            params: {snp:$routeParams.position},
            method: 'GET'
        }).then(
            function(response){
                $scope.target_loss = response.data.target_loss_list
            }
        )
    };

    $scope.fetch_expression = function (lncrna) {
        var normal_array = [];
        var tumor_array = [];
        var x_lable;
        var data='';
        var array=[];
        $http({
            url: base_url + '/api/lncrna_expression_list',
            params: {lncRNA: lncrna, cancer: $routeParams.cancer},
            method: 'GET'
        }).then(
            function (response) {
                console.log(response);
                var express = response.data.lncRNA_expression_list;
                var normal_s;
                var tumor_s;
                var gene_name;
                normal_s = express[0]["normal"].split(',');
                tumor_s = express[0]["tumor"].split(',');
                gene_name = express[0]["gene"];
                for (var i = 0; i < normal_s.length; i++) {
                    normal_array.push(Number(normal_s[i]).toFixed(4))
                }
                for (var i = 0; i < tumor_s.length; i++) {
                    tumor_array.push(Number(tumor_s[i]).toFixed(4))
                }
                array.push(normal_array);
                array.push(tumor_array);
                if (express.length == 1) {
                    data = echarts.dataTool.prepareBoxplotData(array);
                    x_lable = ['Normal'+'('+normal_s.length.toString()+')', 'Tumor'+'('+tumor_s.length.toString()+')']
                } else {
                    var normal_s1 = [];
                    if (express[1]["normal"].indexOf(',')>0){
                        express[1]["normal"].split(',');
                    }
                    var tumor_s1 = express[1]["tumor"].split(',');
                    var array1 = [];
                    var array2 = [];
                    for (var i = 0; i < normal_s1.length; i++) {
                        array1.push(Number(normal_s1[i]).toFixed(4))
                    }
                    for (var i = 0; i < tumor_s1.length; i++) {
                        array2.push(Number(tumor_s1[i]).toFixed(4))
                    }
                    array.push(array1);
                    array.push(array2);
                    data = echarts.dataTool.prepareBoxplotData(array);
                    if ($routeParams.cancer == "GBM") {
                        x_lable = ['Normal_TCGA'+'('+normal_s.length.toString()+')', 'Tumor_TCGA'+'('+tumor_s.length.toString()+')', 'Normal_China'+'('+normal_s1.length.toString()+')', 'Tumor_China'+'('+tumor_s1.length.toString()+')']
                    } else {
                        x_lable = ['Normal_TCGA'+'('+normal_s.length.toString()+')', 'Tumor_TCGA'+'('+tumor_s.length.toString()+')', 'Normal_korea'+'('+normal_s1.length.toString()+')', 'Tumor_korea'+'('+tumor_s1.length.toString()+')']
                    }

                }
                function onClick(params) {
                    console.log(params);
                };
                $scope.lineConfig = {
                    theme: 'default',
                    event: [{click: onClick}],
                    dataLoaded: true
                };

                $scope.lineOption = {
                    title: [
                        {
                            text: gene_name + ' expression in ' + $routeParams.cancer,
                            left: 'center',
                        },
                        {
                            text: 'upper: Q3 + 1.5 * IRQ \nlower: Q1 - 1.5 * IRQ',
                            borderColor: '#999',
                            borderWidth: 1,
                            textStyle: {
                                fontSize: 14
                            },
                            left: '10%',
                            top: '90%'
                        }
                    ],
                    tooltip: {
                        trigger: 'item',
                        axisPointer: {
                            type: 'shadow'
                        }
                    },
                    toolbox: {
                        show : true,
                        feature : {
                            saveAsImage : {show: true}
                        }
                    },
                    grid: {
                        left: '10%',
                        right: '10%',
                        bottom: '15%'
                    },
                    xAxis: {
                        type: 'category',
                        data: x_lable,
                        boundaryGap: true,
                        nameGap: 30,
                        splitArea: {
                            show: false
                        }
                    },
                    yAxis: {
                        name: 'RPKM',
                        type: 'value',
                        splitArea: {
                            show: true
                        }
                    },
                    series: [
                        {
                            name: 'boxplot',
                            type: 'boxplot',
                            data: data.boxData,
                            tooltip: {
                                formatter: function (param) {
                                    return [
                                        'Experiment ' + param.name + ': ',
                                        'upper: ' + Number(param.data[4]).toFixed(4),
                                        'Q3: ' + param.data[3],
                                        'median: ' + param.data[2],
                                        'Q1: ' + param.data[1],
                                        'lower: ' + Number(param.data[0]).toFixed(4)
                                    ].join('<br/>')
                                }
                            }
                        },
                        {
                            name: 'outlier',
                            type: 'scatter',
                            data: data.outliers
                        }
                    ]
                };
            }
        );
    };
    $scope.show_expression = function (lnc_list) {
        $scope.fetch_expression(lnc_list["lncrna"]);
    };
    $scope.fetch_mutation = function () {
        $http({
            url: base_url + '/api/tcga_basic_list',
            params: {cancer: $routeParams.cancer, position: $routeParams.position},
            method: 'GET'
        }).then(
            function (response) {
                console.log(response);
                var info_list;
                info_list = response.data.TCGA_basic_list;
                if (info_list.length>0){
                    $scope.mut_info = info_list[0];
                    $scope.fetch_mut_lnc();
                    if (info_list[0]['gain']!=0){
                        $scope.fetch_target_gain()
                    }
                    if (info_list[0]['loss']!=0){
                        $scope.fetch_target_loss()
                    }
                }
            }
        )
    };
    $scope.fetch_mut_lnc = function () {
        var condition;
        if ($routeParams.position) {
            condition = {cancer: $routeParams.cancer, position: $routeParams.position}
        }
        if ($routeParams.lncrna) {
            condition = {cancer: $routeParams.cancer, lncrna: $routeParams.lncrna}
        }
        $http({
            url: base_url + '/api/tcga_lnc_list',
            params: condition,
            method: 'GET'
        }).then(
            function (response) {
                console.log(response);
                var temp;
                var index;
                temp = response.data.TCGA_lnc_list;
                if (temp.length > 1) {
                    $scope.multiple = 1
                }
                if(temp.length>0){
                    $scope.effect = temp[0]["effect"];
                    $scope.tcga_lnc_list = response.data.TCGA_lnc_list;
                    for (var i = 0; i < temp.length; i++) {
                        if (temp[i]["mut_info"] == $routeParams.position) {
                            index = i;
                        }
                    }
                    $scope.figure = temp[0]["express"];
                    if ( temp[0]["express"]) {
                        $scope.fetch_expression(temp[0]["lncrna"]);
                    }
                }else{
                    $scope.wrong=1
                }

            }
        )
    };
    $scope.fetch_expression_list = function (lncrna) {
        var cancer_type=[];
        var normal_data=[];
        var tumor_data=[];
        $http({
            url: base_url + '/api/lncrna_express_mean',
            params: {lncRNA: lncrna},
            method: 'GET'
        }).then(
            function (response) {
                console.log(response);
                var lncrna_express_list = response.data.lncRNA_expression_mean_list;
                if (lncrna_express_list.length>0){
                    $scope.express=1;
                    for (var i=0;i<lncrna_express_list.length;i++){
                        var temp=lncrna_express_list[i];
                        $scope.lncrna_gene_name=temp['gene'];
                        cancer_type.push(temp["cancer_type"]);
                        normal_data.push(Number(temp["normal"].toFixed(2)));
                        tumor_data.push(Number(temp["cancer"].toFixed(2)))
                    }

                }else{
                    $scope.express=0
                }
                function onClick(params) {
                    console.log(params);
                };
                $scope.lineConfig = {
                    theme: 'default',
                    event: [{click: onClick}],
                    dataLoaded: true
                };
                $scope.lineOption={
                    title : {
                        text: "Expression"
                    },
                    tooltip : {
                        trigger: 'axis',
                    },
                    legend: {
                        data:['Normal','Tumor']
                    },
                    toolbox: {
                        show : true,
                        feature : {
                            magicType : {show: true, type: ['line', 'bar']},
                            restore : {show: true},
                            saveAsImage : {show: true}
                        }
                    },
                    calculable : true,
                    grid: {
                        bottom: '12%',
                        containLabel: true
                    },

                    xAxis : [
                        {
                            axisLabel: {rotate:60,interval:0},
                            type : 'category',
                            data : cancer_type
                        }
                    ],
                    yAxis : [
                        {
                            type : 'value'
                        }
                    ],
                    label:{
                        normal:{
                            show: true,
                            position:'top'}
                    },
                    series : [
                        {
                            name:'Normal',
                            type:'bar',
                            data:normal_data,


                            itemStyle: {
                                normal: {
                                    color: '#00B0F0'
                                }
                            },


                            markLine : {
                                data : [
                                    {type : 'average', name: '平均值'}
                                ]
                            }
                        },
                        {
                            name:'Tumor',
                            type:'bar',
                            data:tumor_data,
                            itemStyle: {
                                normal: {
                                    color: '#9966cc'
                                }
                            },
                            markLine : {
                                data : [
                                    {type : 'average', name : '平均值'}
                                ]
                            }
                        }
                    ]
                }

            }
        );
    };
    $scope.fetch_mut_lnc_list = function () {
        $http({
            url: base_url + '/api/tcga_lnc_list',
            params: {lncrna: $routeParams.lncrna},
            method: 'GET'
        }).then(
            function (response) {
                console.log(response);
                var temp=response.data.TCGA_lnc_list;
                if (temp.length>0){
                    var count_array=[];
                    // $scope.express = temp[0]["home_lnc_search_express"];
                    $scope.tcga_lnc_list = response.data.TCGA_lnc_list;
                    var temp = response.data.TCGA_lnc_list;
                    for (var i=0;i<temp.length;i++){
                        var cancer_name = temp[i]['cancer_type'];
                        var flag=0;
                        for(var j=0;j<count_array.length;j++){
                            if (cancer_name==count_array[j]){
                                flag=1
                            }
                        }
                        if (flag==0){
                            count_array.push(cancer_name)
                        }
                    }
                    $scope.cancer_count = count_array.length;
                    $scope.mut_count = temp.length;
                    console.log(count_array);
                }else{
                    $scope.wrong=1
                }

            })
    };
    $scope.lncrna_detail = function () {
        $http({
            url: base_url+'/api/lncrna_basic_list',
            params: {"lncrna":$routeParams.lncrna},
            method: 'GET'
        }).then(
            function success(response) {
                var lncrna_item;
                var array = [];
                var temp_structure;
                lncrna_item = response.data.lncrna_basic_list;
                if (lncrna_item.length>0){
                    $scope.lncrna = lncrna_item[0];
                    $scope.end = lncrna_item[lncrna_item.length-1]["end"];
                    $scope.gene_alia = response.data.gene_alias;
                    $scope.trans_alia = response.data.trans_alias;
                    $scope.pubmed = response.data.pubmed;
                    temp_structure = lncrna_item[0]["structure"];
                }else{
                    $scope.error = 1
                }
                if (temp_structure.indexOf(",") > 0) {
                    var temp = temp_structure.split(',');
                    var sum_temp=0;
                    array.push({"bottom":0,"width":Number(temp[0].split(':')[0]),"height":Number(temp[0].split(':')[1])});
                    sum_temp+=Number(temp[0].split(':')[0]);
                    for (var i = 1; i < temp.length; i=i+2) {
                        console.log(sum_temp);
                        var temp1 = temp[i].split(':');
                        var temp2 = temp[i+1].split(':');
                        sum_temp += Number(temp1[0])+Number(temp2[0]);
                        array.push({"bottom":3,"width":50,"height":3});
                        array.push({"bottom":0,"width":Number(temp2[0]),"height":Number(temp2[1])});
                    }
                } else {
                    var temp_one = temp_structure.split(':');
                    sum_temp = Number(temp_one[0]);
                    array.push({"bottom":0,"width":Number(temp_one[0]),"height":Number(temp_one[1])});
                }
                $scope.base_num = sum_temp/600;
                $scope.item_size = array;
                $scope.line_width = sum_temp;
                $scope.new_size=array;
            },
            function error(response) {
                $scope.error = 1
            }
        )
    };
    if ($routeParams.cancer) {
        $scope.single=1;
        $scope.cancer_type = $routeParams.cancer;
        $scope.fetch_mutation();

    }
    // if (!($routeParams.cancer) && ($routeParams.lncrna)) {
    //     $scope.all=1;
    //     $scope.lncrna_name=$routeParams.lncrna;
    //     $scope.fetch_mut_lnc_list();
    //     $scope.fetch_expression_list($routeParams.lncrna);
    //     $scope.lncrna_detail()
    //
    // }
}
