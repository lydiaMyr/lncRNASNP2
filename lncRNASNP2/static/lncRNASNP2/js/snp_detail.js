'use strict';

angular.module('lncRNASNP2')
    .controller('SnpDetailController', SnpDetailController)
.directive('ngX', function() {
        return function(scope, elem, attrs) {
            attrs.$observe('ngX', function(x) {
                elem.attr('x', x);
            });
        };
    })
    .directive('ngY', function() {
        return function(scope, elem, attrs) {
            attrs.$observe('ngY', function(y) {
                elem.attr('y', y);
            });
        };
    })
    .directive('ngX1', function() {
        return function(scope, elem, attrs) {
            attrs.$observe('ngX1', function(x1) {
                elem.attr('x1', x1);
            });
        };
    })
    .directive('ngY1', function() {
        return function(scope, elem, attrs) {
            attrs.$observe('ngY1', function(y1) {
                elem.attr('y1', y1);
            });
        };
    })
    .directive('ngX2', function() {
        return function(scope, elem, attrs) {
            attrs.$observe('ngX2', function(x2) {
                elem.attr('x2', x2);
            });
        };
    })
    .directive('ngY2', function() {
        return function(scope, elem, attrs) {
            attrs.$observe('ngY2', function(y2) {
                elem.attr('y2', y2);
            });
        };
    })
    .directive('ngWidth', function() {
        return function(scope, elem, attrs) {
            attrs.$observe('ngWidth', function(width) {
                elem.attr('width', width);
            });
        };
    })
    .directive('ngHeight', function() {
        return function(scope, elem, attrs) {
            attrs.$observe('ngHeight', function(height) {
                elem.attr('height', height);
            });
        };
    });

function SnpDetailController($scope,$routeParams,$http,lncRNASNP2Service) {
    console.log($routeParams.snp);
    $scope.error=0;
    $("[data-toggle='popover']").popover();
    var array = [];
    var name_array=[];
    var line_array=[];
    var max_num = 0;
    var min_start=0;
    var temp_sum=0;
    var base_url = lncRNASNP2Service.getAPIBaseUrl();
    $scope.query_snp = $routeParams.snp;
    $scope.miRNA_effect=false;
    var gain;
    var loss;
    var tag_lable;
    $scope.clear = function () {
      $scope.one=0;
      $scope.two=0;
      $scope.three=0;
      $scope.four=0;
      $scope.five=0;
    };
    $scope.one=1;
    $scope.show_one = function (refer) {
        console.log(refer);
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
    $scope.fetch_gwas = function (snp_info_list,tag_lable) {
        var index=0;
        $http({
            url: base_url+'/api/gwas_ld_list',
            params: {snp:$routeParams.snp},
            method: 'GET'
        }).then(
            function (response) {
                console.log(response);
                var array=[];
                var sum_array=[];
                var temp;
                temp = response.data.gwas_ld_list;
                if (tag_lable){
                    for (var i=0;i<temp.length;i++){
                        console.log(temp[i]["tagsnp"]);
                        if (temp[i]["tagsnp"]==$routeParams.snp) {
                            index=i;
                        }
                    }
                }
                $scope.gwas_ld = temp[index];
                var ld_region = temp[index];
                var asw_s = ld_region["ASW_start"];
                array.push(Number(asw_s));
                var asw_e = ld_region["ASW_end"];
                var ceu_s = ld_region["CEU_start"];
                array.push(Number(ceu_s));
                var ceu_e = ld_region["CEU_end"];
                var chd_s = ld_region["CHD_start"];
                array.push(Number(chd_s));
                var chd_e = ld_region["CHD_end"];
                var gih_s = ld_region["GIH_start"];
                array.push(Number(gih_s));
                var gih_e = ld_region["GIH_end"];
                var lwk_s = ld_region["LWK_start"];
                array.push(Number(lwk_s));
                var lwk_e = ld_region["LWK_end"];
                var mex_s = ld_region["MEX_start"];
                array.push(Number(mex_s));
                var mex_e = ld_region["MEX_end"];
                var mkk_s = ld_region["MKK_start"];
                array.push(Number(mkk_s));
                var mkk_e = ld_region["MKK_end"];
                var tsi_s = ld_region["TSI_start"];
                array.push(Number(tsi_s));
                var tsi_e = ld_region["TSI_end"];
                var yri_s = ld_region["YRI_start"];
                array.push(Number(yri_s));
                var yri_e = ld_region["YRI_end"];
                max_num = Math.max(Number(asw_e),Number(asw_s),Number(ceu_e),Number(ceu_s),Number(chd_e),Number(chd_s),Number(gih_e),Number(gih_s),Number(lwk_e),Number(lwk_s),Number(mex_e),Number(mex_s),Number(mkk_e),Number(mkk_s),Number(tsi_e),Number(tsi_s),Number(yri_e),Number(yri_s));
                var flag=1;
                for(var i=0; i<array.length; i++){
                    if(flag==1 && array[i]!=0){
                        min_start = array[i];
                        flag=0
                        // console.log(min_start)
                    }
                    if(array[i]!=0&&array[i]<min_start){
                        min_start=array[i]
                    }
                };
                for(var i=0; i<snp_info_list.length; i++){
                    var lncrna = snp_info_list[i]['lnc'];
                    var exon_start = snp_info_list[i]['exon_start'];
                    var max_scope = max_num - min_start;
                    name_array.push({"name":lncrna,"y_lable":288+i*20});
                    $scope.lncrna_detail(lncrna,min_start,max_scope,i);
                }
                $scope.asw_width = (Number(asw_e)-Number(asw_s));
                $scope.ceu_width = (Number(ceu_e)-Number(ceu_s));
                $scope.chd_width = (Number(chd_e)-Number(chd_s));
                $scope.gih_width = (Number(gih_e)-Number(gih_s));
                $scope.lwk_width = (Number(lwk_e)-Number(lwk_s));
                $scope.mex_width = (Number(mex_e)-Number(mex_s));
                $scope.mkk_width = (Number(mkk_e)-Number(mkk_s));
                $scope.tsi_width = (Number(tsi_e)-Number(tsi_s));
                $scope.yri_width = (Number(yri_e)-Number(yri_s));
                $scope.asw_start = Number(asw_s);
                $scope.ceu_start = Number(ceu_s);
                $scope.chd_start = Number(chd_s);
                $scope.gih_start = Number(gih_s);
                $scope.lwk_start = Number(lwk_s);
                $scope.mex_start = Number(mex_s);
                $scope.mkk_start = Number(mkk_s);
                $scope.tsi_start = Number(tsi_s);
                $scope.yri_start = Number(yri_s);
            });
    };
    $scope.lncrna_detail = function (lncrna,min_start,max_scope,lncrna_index) {
        $http({
            url: base_url+'/api/lncrna_basic_list',
            params: {"lncrna":lncrna},
            method: 'GET'
        }).then(
            function (response) {
                var lncrna_array = [];
                var end_array = [];
                var sum=0;
                var lncrna_item = response.data.lncrna_basic_list;
                var end_max = lncrna_item[0]['end'];
                var exon_start=lncrna_item[0]['start'];
                for (var i=0;i<lncrna_item.length;i++){
                    var start = Number(lncrna_item[i]["start"]);
                    if (start<exon_start){
                        exon_start=start
                    }
                    var end = Number(lncrna_item[i]["end"]);
                    if(end>end_max){
                        end_max = end
                    }
                    var width = Number(end)-Number(start);
                    array.push({"start":start,"width":width,"y_lable":(280+20*lncrna_index)})
                }
                sum = end_max - exon_start;
                line_array.push({"width":sum,"y_lable":284+20*lncrna_index,"start":exon_start});
                if (sum>temp_sum){
                    temp_sum=sum;
                }
                if (exon_start < min_start){
                    min_start = exon_start;
                }
                if (exon_start-min_start+temp_sum > max_scope){
                    max_scope = exon_start-min_start+temp_sum
                }
                $scope.min_start = min_start;
                $scope.base_num = max_scope/450;
                console.log(min_start);
                /* console.log(max_scope);
                 console.log(max_scope/500);
                 console.log(lncrna_array);*/
                var item_length = lncrna_array;
                //var item_length=[{"width":100,"move":0},{"width":200,"move":30}];
                //array.push({"lncrna": lncrna, "item_size": item_length,"exon_start":exon_start,"line_width":sum});
                $scope.lncrnas = array;
                $scope.name_list = name_array;
                $scope.line_list = line_array;
                console.log(array);
                console.log(line_array);
                console.log(name_array)
            }
        );
    };
    $scope.svg_click = function () {
        console.log("hello world")

    };
    $scope.fetch_gwas_info = function(){
        $http({
            url: base_url+'/api/gwas_basic_list',
            params: {snp:$routeParams.snp},
            method: 'GET'
        }).then(
            function(response){
                console.log(response);
                $scope.gwas_list = response.data.gwas_basic_list
            }
        )
    };
    $scope.fetch_target_gain = function () {
        $http({
            url: base_url+'/api/target_gain_list',
            params: {snp:$routeParams.snp},
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
            params: {snp:$routeParams.snp},
            method: 'GET'
        }).then(
            function(response){
                $scope.target_loss = response.data.target_loss_list
            }
        )
    };
    $scope.modal_title = function (item) {
        $scope.modal_header = "Targe Gain";
        $scope.target = item;
    };
    $scope.modal_title1 = function (item) {
        $scope.modal_header = "Targe Loss";
        $scope.target = item;
    };
    $scope.fetch_snp = function () {
        $http({
            url: base_url+'/api/lncrna_snp_list',
            params: {snp:$routeParams.snp},
            method: 'GET'
        }).then(
            function (response) {
                var snp_info_list;
                snp_info_list = response.data.lncrna_snp_list;
                $scope.lnc_snp = snp_info_list;
                if(snp_info_list.length>0){
                    $scope.snp = snp_info_list[0];
                    tag_lable = snp_info_list[0]['tagSNP'];
                    gain = snp_info_list[0]['gain'];
                    loss = snp_info_list[0]['loss'];
                }else{
                    $scope.error=1
                }

                if (tag_lable){
                    $scope.fetch_gwas(snp_info_list,tag_lable);
                    $scope.fetch_gwas_info();
                }
                if (gain){
                    $scope.fetch_target_gain()
                }
                if (loss){
                    $scope.fetch_target_loss()
                }

            },
            function error(response) {
                $scope.error=1
            }
        )
    };
    $scope.fetch_snp();
}