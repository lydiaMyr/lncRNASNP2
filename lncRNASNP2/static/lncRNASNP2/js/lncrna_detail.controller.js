
'use strict';

angular.module('lncRNASNP2')
    .config(function ($interpolateProvider) {
        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');
    })
    .controller('LncRNAdetailController', LncRNAdetailController);

function LncRNAdetailController($scope,$http,$routeParams,lncRNASNP2Service,$sce) {
    console.log($routeParams.lncrna);
    $("[data-toggle='popover']").popover();
    var base_url = lncRNASNP2Service.getAPIBaseUrl();
    $scope.clear = function () {
        $scope.one=0;
        $scope.two=0;
        $scope.three=0;
        $scope.four=0;
        $scope.five=0;
        $scope.six=0;
    };
    $scope.one=1;
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
         if (refer=="six"){
            $scope.six=1;
            $scope.class_six ="active"
        }
    };
    $scope.fetch_mut_lnc_list = function () {
        $http({
            url: base_url + '/api/tcga_lnc_list',
            params: {lncrna: $routeParams.lncrna},
            method: 'GET'
        }).then(
            function (response) {
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
    $scope.fetch_ncv = function () {
        $http({
            url: base_url+'/api/cosmic_lnc_list',
            params: {lncrna: $routeParams.lncrna},
            method: 'GET'
        }).then(
            function (response) {
                var cnv_info_list;
                cnv_info_list = response.data.cosmic_lnc_list;
                if (cnv_info_list.length>0){
                    $scope.cnv_lnc = cnv_info_list;
                    $scope.mut_count = cnv_info_list.length;
                    $scope.cnv = cnv_info_list[0];
                    if ($routeParams.id_cnv){
                        $scope.effect = cnv_info_list[0]["coding_groups"];
                    }else{
                        $scope.effect=1
                    }
                }else{
                    $scope.error = 1
                }
            },
            function error(response) {
                $scope.error = 1
            }
        )
    };
    $scope.fetch_tcga_target_gain = function () {
        $http({
            url: base_url+'/api/tcga_target_gain_list',
             params: {"lncrna":$routeParams.lncrna},
            method: 'GET'
        }).then(
            function(response){
                $scope.tcga_target_gain = response.data.target_gain_list
            }
        )
    };
    $scope.fetch_tcga_target_loss = function () {
        $http({
            url: base_url+'/api/tcga_target_loss_list',
            params: {"lncrna":$routeParams.lncrna},
            method: 'GET'
        }).then(
            function(response){
                $scope.tcga_target_loss = response.data.target_loss_list
            }
        )
    };
    $scope.fetch_cosmic_target_gain = function () {
        $http({
            url: base_url+'/api/cosmic_target_gain_list',
             params: {"lncrna":$routeParams.lncrna},
            method: 'GET'
        }).then(
            function(response){
                $scope.cosmic_target_gain = response.data.target_gain_list
            }
        )
    };
    $scope.fetch_cosmic_target_loss = function () {
        $http({
            url: base_url+'/api/cosmic_target_loss_list',
            params: {"lncrna":$routeParams.lncrna},
            method: 'GET'
        }).then(
            function(response){
                $scope.cosmic_target_loss = response.data.target_loss_list
            }
        )
    };
    $scope.fetch_expression_list = function () {
        var cancer_type=[];
        var normal_data=[];
        var tumor_data=[];
        $http({
            url: base_url + '/api/lncrna_express_mean',
            params: {"lncRNA":$routeParams.lncrna},
            method: 'GET'
        }).then(
            function (response) {
                console.log("fetch expression");
                var lncrna_express_list = response.data.lncRNA_expression_mean_list;
                if (lncrna_express_list.length>0){
                    $scope.express=1;
                    console.log("get expression");
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
                    };
                    $scope.lineConfig = {
                        theme: 'default',
                        event: [{click: onClick}],
                        dataLoaded: true
                    };
                    $scope.lineOption={
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
                                name: 'RPKM',
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
                    // $scope.fetch_expression_list();
                    if (lncrna_item[0]["snp_count"]>0){
                        $scope.lncrna_snp_list();
                    }
                    if (lncrna_item[0]["gain"]>0){
                        $scope.fetch_target_gain();
                    }
                    if (lncrna_item[0]["loss"]>0){
                        $scope.fetch_target_loss();
                    }
                    if (lncrna_item[0]["tcga_count"]>0){
                        $scope.fetch_mut_lnc_list();
                    }
                    if (lncrna_item[0]["cosmic_count"]>0){
                        $scope.fetch_ncv()
                    }
                    if (lncrna_item[0]["tcga_gain"]>0){
                        $scope.fetch_tcga_target_gain();
                    }
                    if (lncrna_item[0]["tcga_loss"]>0){
                        $scope.fetch_tcga_target_loss();
                    }
                    if (lncrna_item[0]["cosmic_gain"]>0){
                        $scope.fetch_cosmic_target_gain();
                    }
                    if (lncrna_item[0]["cosmic_loss"]>0){
                        $scope.fetch_cosmic_target_loss();
                    }
                    if (lncrna_item[0]["express"]>0){
                        $scope.fetch_expression_list();
                        $scope.express = 1
                    }

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
                // var array1=[{"start":10,"end":8,"mirna":"test_mirna","length_num":0},{"start":100,"end":7,"mirna":"test_mirna","length_num":13},{"start":70,"end":7,"mirna":"test_mirna","length_num":13},{"start":90,"end":8,"mirna":"test_mirna","length_num":12},{"start":90,"end":8,"mirna":"test_mirna","length_num":12},{"start":80,"end":6,"mirna":"test_mirna","length_num":14}];
                // var array2=[{"start":10,"end":8,"mirna":"test_mirna"},{"start":70,"end":7,"mirna":"test_mirna"},{"start":70,"end":7,"mirna":"test_mirna"},{"start":60,"end":8,"mirna":"test_mirna"},{"start":90,"end":8,"mirna":"test_mirna"},{"start":40,"end":6,"mirna":"test_mirna"}];
                // var array3=[{"start":10,"end":8,"mirna":"test_mirna"},{"start":70,"end":7,"mirna":"test_mirna"},{"start":70,"end":7,"mirna":"test_mirna"},{"start":60,"end":8,"mirna":"test_mirna"},{"start":90,"end":8,"mirna":"test_mirna"},{"start":40,"end":6,"mirna":"test_mirna"}];
                // $scope.mirna_target=[array1,array2,array3];
                // console.log(array3)
            },
            function error(response) {
                $scope.error = 1
            }
        )
    };
    $scope.lncrna_detail();
    $scope.lncrna_snp_list = function () {
        $http({
            url: base_url+'/api/lncrna_snp_list',
            params: {"lncrna":$routeParams.lncrna},
            method: 'GET'
        }).then(
            function success(response){
                $scope.lncrna_snp_item = response.data.lncrna_snp_list;
            },
            function error(response) {
                console.log("something error happens!");
            }
        )
    };
    $scope.show_target_detail = function (target) {
        $scope.mirna_target = target;
    };
    $scope.fetch_target_gain = function () {
        $http({
            url: base_url+'/api/target_gain_list',
            params: {"lncrna":$routeParams.lncrna},
            method: 'GET'
        }).then(
            function(response){
                $scope.target_gain = response.data.target_gain_list
            }
        )
    };

    $scope.fetch_target_loss = function () {
        $http({
            url: base_url+'/api/target_loss_list',
            params: {"lncrna":$routeParams.lncrna},
            method: 'GET'
        }).then(
            function(response){
                console.log(response);
                $scope.target_loss = response.data.target_loss_list
            }
        )
    };

    $scope.modal_title = function (item) {
        $scope.modal_header = "Target Gain";
        $scope.target = item;
    };
    $scope.modal_title1 = function (item) {
        $scope.modal_header = "Target Loss";
        $scope.target = item;
    };
    $scope.toggle_track = function (track_name) {
        $('svg.' + track_name).toggle();
    };
    $scope.tracks_controller_flag = false;
    $scope.cons_track_flag = true;
    $scope.expr_track_flag = true;
    $scope.hexp_track_flag = true;
    $scope.lexp_track_flag = true;
    var load_tracks = function () {
        $http({
            url: base_url+"/api/tracks",
            params: {"lncrna":$routeParams.lncrna}
        }).then(
            function success(response) {
                $scope.tracks = response.data;
                $scope.lncrna_mirna_tracks = $sce.trustAsHtml($scope.tracks.tracks);
                // $scope.lncrna_track = $sce.trustAsHtml($scope.tracks.lncrna_track);
                // $scope.cons_track = $sce.trustAsHtml($scope.tracks.cons_track);
                // $scope.expr_track = $sce.trustAsHtml($scope.tracks.expr_track);
                // $scope.hexp_track = $sce.trustAsHtml($scope.tracks.hexp_track);
                // $scope.lexp_track = $sce.trustAsHtml($scope.tracks.lexp_track);
            },
            function error() {
                console.log("something error happens");
            }
        )
    };
    load_tracks();
}
