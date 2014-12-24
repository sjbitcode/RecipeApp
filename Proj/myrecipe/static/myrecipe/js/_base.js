var utils = {} || utils;

// For each error in the errors list, wrap error in 'p' element
// and append it to #alertBox.
utils.appendErrors = function(errors, f) {
  $("#alertBoxInner").html("");
  
  _.each(errors, function(el, i) {
    $("<p>").text((i + 1) + ". " + el).appendTo("#alertBoxInner");
  });
  
  if(f && typeof(f) == "function")
    f();
  
};

// Takes an Error object, gets all values from it, and flattens if to a single array.
/*
   Error object will look like this:
   var errors = {
     "title" :["Title cannot be empty."],
     "url"   :["Please enter a valid Url."],
     "tags"  :["You cannot have more than 10 tags."]
   };
*/
utils.buildErrors = function(errorObj) {
  return _.flatten(_.values(errorObj));
};

utils.clearAll = function() {
  $("#alertBox").hide();
  $("#successBox").hide();
}

utils.showAlert = function() {
  $("#alertBox").fadeIn();
};

utils.showSuccess = function() {
  $("#successBox").fadeIn();
}

// Takes an error object, appends the errors, and shows the alert.
utils.comboAlert = function(x) {
  utils.clearAll();
  x = x.responseJSON || x;
  utils.appendErrors(utils.buildErrors(x), function() {
    utils.showAlert();
  });
};

// Takes a message, appends it to success box, and shows the success box.
utils.comboSuccess = function(x) {
  utils.clearAll();
  $("#successBoxInner").html("");
  $("<p>").text(x).appendTo("#successBoxInner");
  utils.showSuccess();
};