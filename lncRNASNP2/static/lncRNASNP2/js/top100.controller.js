"use strict";

angular.module('lncRNASNP2')
    .controller('SnpTopController', SnpTopController);

function SnpTopController($scope,$http,$window,$routeParams) {
    $scope.fetch_snp_effect = function () {
        $http({
            url: '/api/snp_effect_list',
            method: 'GET'
        }).then(
            function (response) {
                console.log(response);
                $scope.snp_effect_list = response.data.snp_effect_list;
            }
        )
    };
}
