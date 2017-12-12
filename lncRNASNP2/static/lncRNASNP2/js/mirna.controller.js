'use strict';

angular.module('lncRNASNP2')
    .controller('MirnaController', MirnaController);

function MirnaController($scope,$http,$routeParams,$window,lncRNASNP2Service) {
    console.log("MirnaController loaded");
    $scope.vmirna = "hello world";
    var base_url = lncRNASNP2Service.getAPIBaseUrl();
    $scope.mirna_expression = function () {
        $scope.choose = false;
        $http({
            url: base_url+'/api/mir_expression_list',
            method: 'GET'
        }).then(
            function (response) {
                console.log(response);
                var htemp,mtemp,ltemp,vtemp;
                $scope.hmirnas_collections = response.data.hmirna_list;
                htemp = response.data.hmirna_list;
                $scope.hmirna_init = htemp[0].miRNA;
                $scope.mmirnas_collections = response.data.mmirna_list;
                mtemp = response.data.mmirna_list;
                $scope.mmirna_init = mtemp[0].miRNA;
                $scope.lmirnas_collections = response.data.lmirna_list;
                ltemp = response.data.lmirna_list;
                $scope.lmirna_init = ltemp[0].miRNA;
                $scope.vmirnas_collections = response.data.vmirna_list;
                vtemp = response.data.vmirna_list;
                $scope.vmirna_init = vtemp[0].miRNA;
            }
        )
    };
    $scope.mirna_expression();
    $scope.show_detail = function (mirna) {
        if (mirna=="hmirna"){
            mirna=$("#hmirna option:selected").text();
        }
        if (mirna=="mmirna"){
            mirna=$("#mmirna option:selected").text();
        }
        if (mirna=="lmirna"){
            mirna=$("#lmirna option:selected").text();
        }
        if (mirna=="vmirna"){
            mirna=$("#vmirna option:selected").text();
        }
        $window.open("#!/mirna_info?mirna="+mirna+'&snp=0',"_self");
    };
    $scope.show_snp_target = function (mirna) {
        if (mirna=="hmirna"){
            mirna=$("#hmirna option:selected").text();
        }
        if (mirna=="mmirna"){
            mirna=$("#mmirna option:selected").text();
        }
        if (mirna=="lmirna"){
            mirna=$("#lmirna option:selected").text();
        }
        if (mirna=="vmirna"){
            mirna=$("#vmirna option:selected").text();
        }
        $window.open("#!/mirna_info?mirna="+mirna+'&snp=1',"_self");
    };
}


