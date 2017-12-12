"use strict";

angular.module('lncRNASNP2', ['ui.bootstrap', 'ngRoute','tableSort', 'pageslide-directive','ngSanitize','ui.bootstrap-slider','bw.paging','angularTreeview', 'ng-echarts'])
    .config(function ($routeProvider) {
        $routeProvider
            .when("/", {
                templateUrl: "/static/lncRNASNP2/pages/home.html",
                controller: "HomeController",
            })
            .when("/document", {
                templateUrl: "/static/lncRNASNP2/pages/document.html",
                controller: "ContactController",
            })
            .when("/download", {
                templateUrl: "/static/lncRNASNP2/pages/download.html",
                controller: "DownloadController",
            })
            .when("/contact", {
                templateUrl: "/static/lncRNASNP2/pages/contact.html",
                controller: "ContactController",
            })
            .when("/search", {
                templateUrl: "/static/lncRNASNP2/pages/quick_search.html",
                controller: "SearchPageController",
            })
            .when("/key", {
                templateUrl: "/static/lncRNASNP2/pages/test.html",
                controller: "TestController",
            })
            .when("/mre_graph", {
                templateUrl: "/static/lncRNASNP2/pages/test_page.html",
                controller: "TestPageController",
            })
            .when("/snp", {
                templateUrl: "/static/lncRNASNP2/pages/snp.html",
                controller: "SnpController",
            })
            .when("/lncrna", {
                templateUrl: "/static/lncRNASNP2/pages/lncrnas.html",
                controller: "LncRNAController",
            })
            .when("/lncrna_info", {
                templateUrl: "/static/lncRNASNP2/pages/lncrna_detail.html",
                controller: "LncRNAdetailController",
            })
            .when("/mirna", {
                templateUrl: "/static/lncRNASNP2/pages/mirna.html",
                controller: "MirnaController",
            })
            .when("/mirna_info", {
                templateUrl: "/static/lncRNASNP2/pages/mirna_detail.html",
                controller: "MirnaDetailController",
            })
            .when("/gene", {
                templateUrl: "/static/lncRNASNP2/pages/gene.html",
                controller: "GeneController",
            })
            .when("/snp_info", {
                templateUrl: "/static/lncRNASNP2/pages/snp_detail.html",
                controller: "SnpDetailController",
            })
            .when("/snp_effect", {
                templateUrl: "/static/lncRNASNP2/pages/top100.html",
                controller: "SnpTopController",
            })
            .when("/tcga_home", {
                templateUrl: "/static/lncRNASNP2/pages/tcga_home.html",
                controller: "TcgaHomeController",
            })
            .when("/tcga_mutation", {
                templateUrl: "/static/lncRNASNP2/pages/tcga_mutation.html",
                controller: "TcgaMutationController",
            })
            .when("/tcga_mutation_info", {
                templateUrl: "/static/lncRNASNP2/pages/tcga_mutation_detail.html",
                controller: "TcgaMutationDetailController",
            })
            .when("/cosmic_ncv", {
                templateUrl: "/static/lncRNASNP2/pages/cosmic_ncv.html",
                controller: "CosmicController",
            })
            .when("/cosmic_info", {
                templateUrl: "/static/lncRNASNP2/pages/cosmic_detail.html",
                controller: "CosmicDetailController",
            })
            .when("/ld_region", {
                templateUrl: "/static/lncRNASNP2/pages/LD_region.html",
                controller: "SearchController",
            })
            .when("/query_lnc", {
                templateUrl: "/static/lncRNASNP2/pages/echarts.html",
                controller: "LineController",
            })
             .when("/target", {
                templateUrl: "/static/lncRNASNP2/pages/target.html",
                 controller: "TargetController",
            })
            .otherwise({
                redirectTo: "/404.html",
            });
    })
    .config(function ($interpolateProvider) {
        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');
    })
    .config( [
        '$compileProvider',
        function( $compileProvider )
        {
            $compileProvider.aHrefSanitizationWhitelist(/^\s*(https?|ftp|mailto|tel|file|sms):/);
            // Angular v1.2 之前使用 $compileProvider.urlSanitizationWhitelist(...)
        }
    ])
.service('lncRNASNP2Service',function () {
    this.getBrowserBaseUrl = function () {
        return "http://211.69.207.247/wubrowse/browser/?genome=hg38";
    };
    this.getBrowserDataHubNaseUrl = function () {
        // return "211.69.207.247/lncRNASNP2";
        return "0.0.0.0:3000";
    };
    this.getAPIBaseUrl = function () {
        //return "/lncRNASNP2"
        return ""
    }
});
