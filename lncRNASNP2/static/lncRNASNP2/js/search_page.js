"use strict";

angular.module('lncRNASNP2')
    .controller('SearchPageController', SearchPageController);

function SearchPageController($scope,$http,$window,$routeParams,lncRNASNP2Service) {
    console.log("SearchPageController loaded");
    $scope.content = "human";
    var lnc_name;
    var name_list=[];
    var base_url = lncRNASNP2Service.getAPIBaseUrl();
    var subjects=["rs1001021","rs934","rs7069"];
    $('#search').typeahead({source: subjects});
    var flag=0;
    $scope.check = function (query_item) {
        if(/[@#\$%\^&\*]+/g.test(query_item)){
            alert("Invalid input");
            flag=1;
            history.back();
        }
    };
    $scope.filter_snp = function(){
        var snp_num = $("#query_snp").val();
        $scope.check(snp_num);
        if(flag==0){
            window.open(base_url+"#!/snp_info?snp="+snp_num,"_self")
        }
    };
    $scope.filter_lncrna = function () {
        var query_lnc = $("#query_lncrna").val();
        $scope.check(query_lnc);
         if(flag==0){
             if(query_lnc.indexOf('NONHSAT')==0){
                 window.open(base_url+"#!/lncrna_info?lncrna="+query_lnc,"_self")
             }else {
                 $scope.filter_lncrna_alias(query_lnc)
             }
         }
    };
     $scope.filter_lncrna_alias = function (query_item) {
        $http({
            url: base_url+'/api/lncrna_match_result',
            params: {"lncrna":query_item},
            method: 'GET'
        }).then(
            function success(response) {
                var temp = response.data.match_result;
                if (temp.length>0){
                    window.open(base_url+"#!/query_lnc?lncrna="+query_item,"_self")
                }
                if(temp.length==0){
                    $scope.alert_show=1
                }
            });
    };
    $scope.filter_mirna = function () {
        var mirna_num = $("#query_mirna").val();
        $scope.check(mirna_num);
        if(flag==0){
            window.open(base_url+"#!/key?mirna="+mirna_num)
        }

        // window.open(base_url+"#!/mirna_info?mirna="+mirna_num,"_self")
    };
    $scope.filter_tagsnp = function () {
        var tagsnp = $("#query_tagsnp option:selected").text();
        $scope.check(tagsnp);
        if(flag==0){
             window.open(base_url+"#!/snp_info?snp="+tagsnp,"_self")
        }

    };
    $scope.filter_cancer = function () {
        var options=$("#query_cancer option:selected");
        var cancer = options.text();
        $scope.check(cancer);
        if(flag==0){
             window.open(base_url+"#!/tcga_mutation?cancer="+cancer,"_self")
        }

    };

    $scope.filter_cosmic = function () {
        var cosmic_id =  $("#query_cosmic_id").val();
        $scope.check(cosmic_id);
        if(flag==0){
            window.open(base_url+"#!/cosmic_info?id_cnv="+cosmic_id,"_self")
        }

    };
    $scope.filter_cosmic_lncrna = function () {
        var lncrna =  $("#query_cosmic_lncrna").val();
        $scope.check(lncrna);
        if(flag==0){
            window.open(base_url+"#!/cosmic_info?lncrna="+lncrna,"_self")
        }
    };
    $scope.ld_region = function () {
        var position_query = $("#query_position").val();
        $scope.check(position_query);
        if(flag==0){
            var chr,start,end;
            var item=position_query.split(":");
            chr = item[0];
            var pos=item[1].split("-");
            start = pos[0];
            end = pos[1];
            window.open(base_url+"#!/ld_region?chromosome="+chr+"&start="+start+"&end="+end,"_self")
        }

    };
    $scope.batch_search = function () {
        var queryitem = $("#search_content").val();
        $scope.check(queryitem);
        if(flag==0){
            var query_ls = queryitem.split('\n');
            if($("#snp").is(":checked")){
                window.open(base_url+"#!/ld_region?snp="+query_ls,"_self")
            }
            if($("#mirna").is(":checked")){
                window.open(base_url+"#!/ld_region?mirna="+query_ls,"_self")
            }
            if($("#lncrna").is(":checked")){
                window.open(base_url+"#!/ld_region?lncrna="+query_ls,"_self")
            }
        }
    };

    $scope.fetch_tagSNP = function () {
        $http({
            url: base_url+'/api/gwas_ld_list',
            method: 'GET'
        }).then(
            function (response) {
                console.log(response);
                $scope.tagSNP_list = response.data.tagSNP_list;
            }
        )
    };
    $scope.fetch_tagSNP();
}

