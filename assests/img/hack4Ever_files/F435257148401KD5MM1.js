var lift_settings = {};
window.lift.extend(lift_settings,window.liftJQuery);
window.lift.extend(lift_settings,{"liftPath": "/lift", "ajaxRetryCount": 3, "ajaxPostTimeout": 5000, "gcPollingInterval": 75000, "gcFailureRetryTimeout": 15000, "cometGetTimeout": 140000, "cometFailureRetryTimeout": 10000, "cometServer": null, "logError": function(msg) {}, "ajaxOnFailure": function() {alert("The server cannot be contacted at this time");}, "ajaxOnStart": function() {jQuery('#'+"ajax-loader").show();}, "ajaxOnEnd": function() {jQuery('#'+"ajax-loader").hide();}});
window.lift.init(lift_settings);
var destroy_F435257148203RGCHVN = function() {}
var destroy_F435257148216KCMIMQ = function() {}
var destroy_F435257148230PEUGUT = function() {}
var destroy_F435257148234CZDW2I = function() {}
var destroy_F435257148246PEKAMA = function() {}
jQuery(document).ready(function() {lift.registerComets({"F435257148216KCMIMQ": 435257148403, "F435257148203RGCHVN": 435257148219, "F435257148230PEUGUT": 435257148402, "F435257148234CZDW2I": 435257148404, "F435257148246PEKAMA": 435257148382},true);});