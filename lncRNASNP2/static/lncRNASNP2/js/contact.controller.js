'use strict';

angular.module('lncRNASNP2')
    .controller('ContactController', ContactController)
    .directive('email2image', email2image);

function ContactController($scope) {
    console.log("ContactController loaded");
}
function email2image() {
    return {
        restrict: 'EA',
        template: '<canvas style="margin-bottom: -7px;"></canvas>',
        link: function (scope, element, attrs) {
            scope.canvas = element.find('canvas')[0];
            scope.canvas.height = attrs.height;
            scope.canvas.width = attrs.width;
            scope.context = scope.canvas.getContext('2d');
            scope.context.font="16px Arial";
            scope.context.fillStyle = '#36486b';
            scope.context.fillText(attrs.email, 2,16);
        }
    }
}