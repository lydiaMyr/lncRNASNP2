'use strict';

angular.module('lncRNASNP2')
    .controller('LncRNAController', LncRNAController)
    .controller('GeneController', GeneController);

function LncRNAController($scope,$http,$routeParams,lncRNASNP2Service) {
    $scope.chr_num = $routeParams.chromosome;
    var base_url = lncRNASNP2Service.getAPIBaseUrl();
    $("[data-toggle='popover']").popover();
    $scope.fetch_lncrna = function () {
        $http({
            url: base_url+'/api/lncrna_gene_list',
            params: {chromosome:$routeParams.chromosome},
            method: 'GET'
        }).then(
            function (response) {
                console.log(response);
                $scope.records_number = response.data.records_number;
                $scope.lncrna_gene_list = response.data.lncrna_gene_list;
            }
        )
    };
    $scope.fetch_lncrna();
    $scope.update_page = function (test,page,size,total) {
        $http({
            url: base_url+'/api/lncrna_gene_list',
            params: {page:page,chromosome:$routeParams.chromosome},
            method: 'GET'
        }).then(
            function (response) {
                $scope.lncrna_gene_list = response.data.lncrna_gene_list;
            }
        )
    };

}

function GeneController($scope,$http,$routeParams,lncRNASNP2Service) {
    var base_url = lncRNASNP2Service.getAPIBaseUrl();
     $scope.fetch_gene = function () {
        $http({
            url: base_url+'/api/gene',
            params: {gene:$routeParams.gene},
            method: 'GET'
        }).then(
            function (response) {
                console.log(response);
                var temp = response.data.transcripts_list;
                if (temp.length==0){
                    $scope.error=1
                }else{
                      $scope.gene = temp[0]['gene'];
                      $scope.trans_list = temp
                }

            }
        )
    };
    $scope.fetch_gene()
}
