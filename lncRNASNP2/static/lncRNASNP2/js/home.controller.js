"use strict";

angular.module('lncRNASNP2')
    .controller('HomeController', HomeController);

function HomeController($scope,$http,$window,$routeParams,lncRNASNP2Service) {
    console.log("HomeController loaded");
    $scope.content = "human";
    $(".alert").alert();
    var lnc_name;
    var name_list=[];
    var base_url = lncRNASNP2Service.getAPIBaseUrl();
    var subjects=["rs1001021","rs2642","rs7069","NONHSAT000024.2","ENST00000515242"];
    $('#search').typeahead({source: subjects});
    $(document).keyup(function(event){
        if(event.keyCode ==13){
            $("#search_button").trigger("click");
        }
    });
    var flag=0;
    var cancer_ls=["ACC","BLCA","BRCA","CESC","CHOL","COAD","DLBC","ESCA","GBM","HNSC","KICH","KIRC","KIRP","LAML","LGG","LIHC","LUAD","LUSC","OV",
        "PAAD","PCPG","PRAD","READ","SARC","SKCM","STAD","TGCT","THCA","THYM","UCEC","UCS","UVM"];
    $scope.search_query = function () {
        var query_item = $('#search').val();
        if(/[@#\$%\^&\*]+/g.test(query_item)){
            alert("Invalid input");
            flag=1;
            history.back();
        }
        if(flag==0){
            if (query_item.indexOf("rs")==0){
                $scope.filter_snp(query_item)
            }
            if (query_item.indexOf("NONHSAT")==0){
                $scope.filter_lncrna(query_item)
            }
            if (query_item.indexOf("NONHSAG")==0){
                $scope.filter_gene(query_item)
            }
            if (query_item.indexOf("hsa")==0 || query_item.indexOf("miR")==0 ){
                $scope.filter_mirna(query_item)
            }
            if (cancer_ls.indexOf(query_item)>=0){
                $scope.filter_cancer(query_item)
            }
            if (query_item.indexOf("COSN")==0){
                $scope.filter_cosmic(query_item)
            }
            if (query_item.indexOf("chr")==0){
                $scope.ld_region(query_item)
            }
            if (!(query_item.indexOf("rs")==0)&&!(query_item.indexOf("NONH")==0)&&!(query_item.indexOf("hsa")==0 || query_item.indexOf("miR")==0)&&(!(cancer_ls.indexOf(query_item)>=0))&&(!query_item.indexOf("COSN")==0)&&(!query_item.indexOf("chr")==0)){
                $scope.filter_lncrna_alias(query_item);
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
                    $scope.alert_show=1;
                    $('#alert').show()
                }
            });
    };

    $scope.filter_snp = function(query_snp){
        window.open(base_url+"#!/snp_info?snp="+query_snp,"_self")
    };
    $scope.filter_lncrna = function (query_lnc) {
        if(query_lnc.indexOf('.')>=0||query_lnc.indexOf("ENST")==0){
            window.open(base_url+"#!/lncrna_info?lncrna="+query_lnc,"_self")
        }else {
            window.open(base_url+"#!/query_lnc?lncrna="+query_lnc)
        }
    };
    $scope.filter_gene = function (query_gene) {
        window.open(base_url+"#!/gene?gene="+query_gene,"_self")
    };
    $scope.filter_mirna = function (query_miR) {
        window.open(base_url+"#!/key?mirna="+query_miR)
        // window.open(base_url+"#!/mirna_info?mirna="+query_miR,"_self")
    };
    $scope.filter_cancer = function (cancer) {
        window.open(base_url+"#!/tcga_mutation?cancer="+cancer,"_self")
    };
    $scope.filter_cosmic = function (cosmic_id) {
        window.open(base_url+"#!/cosmic_info?id_cnv="+cosmic_id,"_self")
    };
    $scope.ld_region = function (position_query) {
        var chr,start,end;
        var item=position_query.split(":");
        chr = item[0];
        var pos=item[1].split("-");
        start = pos[0];
        end = pos[1];
        window.open(base_url+"#!/ld_region?chromosome="+chr+"&start="+start+"&end="+end,"_self")
    };
}
