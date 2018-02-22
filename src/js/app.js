//   angular.module('myApp', ['ngMaterial'])
//   .config(function($mdThemingProvider) {
//     $mdThemingProvider.theme('default')
//       .primaryPalette('blue', {
//         'default': '400',
//         'hue-1': '100',
//         'hue-2': '600',
//         'hue-3': 'A100'
//       })
//       .accentPalette('orange')
//       .warnPalette('yellow')
//       .backgroundPalette('grey');
//   });

angular.module('aloMundo', ['ngMaterial']).controller('ToastEx', function($scope, $mdToast) {
$mdToast.show(
        $mdToast.simple('Alô Mundo Toast!')
        .position('left bottom')
        .hideDelay(3000)
);
});