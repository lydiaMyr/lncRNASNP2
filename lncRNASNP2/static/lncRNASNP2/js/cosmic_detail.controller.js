'use strict';

angular.module('lncRNASNP2')
    .controller('CosmicDetailController', CosmicDetailController);

function CosmicDetailController($scope,$http,$routeParams,lncRNASNP2Service) {
    console.log("CosmicDetailController loaded");
    $scope.clear = function () {
        $scope.one=0;
        $scope.two=0;
        $scope.three=0;
        $scope.four=0;
        $scope.five=0;
    };
    $scope.modal_title = function (item) {
        $scope.modal_header = "Target Gain";
        $scope.target = item;
    };
    $scope.modal_title1 = function (item) {
        $scope.modal_header = "Target Loss";
        $scope.target = item;
    };
    $scope.one=1;
    $scope.fetch_target_gain = function () {
        $http({
            url: base_url+'/api/cosmic_target_gain_list',
            params: {snp:$routeParams.id_cnv},
            method: 'GET'
        }).then(
            function(response){
                $scope.target_gain = response.data.target_gain_list
            }
        )
    };
    $scope.fetch_target_loss = function () {
        $http({
            url: base_url+'/api/cosmic_target_loss_list',
            params: {snp:$routeParams.id_cnv},
            method: 'GET'
        }).then(
            function(response){
                $scope.target_loss = response.data.target_loss_list
            }
        )
    };
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
    var base_url = lncRNASNP2Service.getAPIBaseUrl();
    $("[data-toggle='popover']").popover();
    $scope.fetch_cnv = function (condition) {
        $http({
            url: base_url+'/api/cosmic_lnc_list',
            params: {ncv_id:$routeParams.id_cnv},
            method: 'GET'
        }).then(
            function (response) {
                var cnv_info_list;
                cnv_info_list = response.data.cosmic_lnc_list;
                if (cnv_info_list.length>0){
                    $scope.cnv_lnc = cnv_info_list;
                    $scope.mut_count = cnv_info_list.length;
                    $scope.cnv = cnv_info_list[0];
                    if (cnv_info_list[0]["gain"]){
                        $scope.fetch_target_gain()
                    }
                    if (cnv_info_list[0]["loss"]){
                        $scope.fetch_target_loss()
                    }
                    $scope.effect = cnv_info_list[0]["noncoding_groups"];
                }else {
                    $scope.error = 1
                }
            },
            function error(response) {
                $scope.error = 1
            }
        )
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
    $scope.query_cnv=1;
    $scope.query_cnv = $routeParams.id_cnv;
    $scope.fetch_cnv()
}

