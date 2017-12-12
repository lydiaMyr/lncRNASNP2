'use strict';

angular.module('lncRNASNP2')
    .controller('CosmicController', CosmicController);

function CosmicController($scope,$http,$routeParams,lncRNASNP2Service) {
    console.log("CosmicController loaded");
    console.log($scope.currentPage);
     $("[data-toggle='popover']").popover();
    var base_url = lncRNASNP2Service.getAPIBaseUrl();
    var chr_num = $("#chr_num option:selected").text();
    $scope.fetch_cosmic_ncv_list = function () {
        chr_num = $("#chr_num option:selected").text();
        $http({
            url: base_url+'/api/cosmic_lnc_list',
            params: {chr:chr_num},
            method: 'GET'
        }).then(
            function (response) {
                console.log(response);
                $scope.selected_chr=chr_num;
                $scope.cosmic_lnc_list = response.data.cosmic_lnc_list;
                $scope.records_number = response.data.records_number;
            }
        )
    };
    $scope.update_page = function (test,page,size,total) {
        $http({
            url: base_url+'/api/cosmic_lnc_list',
            params: {page:page,chr:chr_num},
            method: 'GET'
        }).then(
            function (response) {
                $scope.cosmic_lnc_list = response.data.cosmic_lnc_list;
            }
        )
    };

   $scope.fetch_cosmic_ncv_list();
}