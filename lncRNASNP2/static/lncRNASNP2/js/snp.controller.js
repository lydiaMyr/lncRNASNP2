'use strict';

angular.module('lncRNASNP2')
    .controller('SnpController', SnpController);
function SnpController($scope,$http,$window,$routeParams,lncRNASNP2Service) {
    console.log("SnpController loaded");
    $("[data-toggle='popover']").popover();
    $scope.miRNA_effect=$("#target").is(":checked");
    $scope.snp = $routeParams.snp;
    var base_url = lncRNASNP2Service.getAPIBaseUrl();
    $scope.search_click = function (position_query,gmaf) {
        var condition = {};
        if (position_query){
            if (position_query.indexOf(":") >= 0){
                console.log(position_query);
                var chr,start,end;
                var item=position_query.split(":");
                chr = item[0];
                var pos=item[1].split("-");
                start = pos[0];
                end = pos[1];
                condition['chr'] = chr;
                condition['start'] = Number(start);
                condition['end'] = Number(end)
            }
            else{
                chr = position_query;
                condition["chr"] = chr
            }
        }
        var g_factor = $("#gmaf option:selected").text();
        if (g_factor!="ALL"){
            condition["gmaf"]=g_factor
        }
       if ($("#ld").is(":checked")){
            condition["ld"]=1
        }
        if ($("#effect").is(":checked")){
            condition["effect"] = 1
        }
        if ($("#target").is(":checked")) {
            condition["target"] = 1
        }
        if($("#exp").is(":checked")){
            condition["exp"]=1
        }
        $http({
            url: base_url+'/api/lncrna_snp_list',
            params: condition,
            method: 'GET'
        }).then(
            function (response) {
                var temp = response.data.lncrna_snp_list;
                console.log(temp.length);
                if (temp.length==0){
                    $scope.error=1
                }
                $scope.records_number = response.data.records_number;
                $scope.lncrna_snp_list = response.data.lncrna_snp_list;
            }
        )
    };
    $scope.check_query = function () {
        $scope.miRNA_effect=$("#target").is(":checked");
    };
    $scope.fetch_snp = function () {
        $http({
            url: base_url+'/api/lncrna_snp_list',
            method: 'GET'
        }).then(
            function (response) {
                console.log(response);
                $scope.records_number = response.data.records_number;
                $scope.lncrna_snp_list = response.data.lncrna_snp_list;
            }
        )
    };
    $scope.fetch_snp();
    $scope.update_page = function (test,page,size,total) {
        var position_query = $scope.position_query;
        var condition = {};
        if (position_query){
            if (position_query.indexOf(":") >= 0){
                console.log(position_query);
                var chr,start,end;
                var item=position_query.split(":");
                chr = item[0];
                var pos=item[1].split("-");
                start = pos[0];
                end = pos[1];
                condition['chr'] = chr;
                condition['start'] = Number(start);
                condition['end'] = Number(end)
            }
            else{
                chr = position_query;
                condition["chr"] = chr
            }
        }
        var g_factor = $("#gmaf option:selected").text();
        if (g_factor!="ALL"){
            condition["gmaf"]=g_factor
        }
        if ($("#ld").is(":checked")){
            condition["ld"]=1
        }
        if ($("#effect").is(":checked")){
            condition["effect"] = 1
        }
        if ($("#target").is(":checked")) {
            condition["target"] = 1
        }
        if($("#exp").is(":checked")){
            condition["exp"]=1
        }
        condition["page"] = page;
        $http({
            url: base_url+'/api/lncrna_snp_list',
            params: condition,
            method: 'GET'
        }).then(
            function (response) {
                $scope.lncrna_snp_list = response.data.lncrna_snp_list;
            }
        )
    };
}
