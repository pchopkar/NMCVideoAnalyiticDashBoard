$(document).ready(function () {
  $("#medicalcollegelist").selectpicker();
  $("#CameraLocationArea").selectpicker();

  $("#CameraLocationSubArea").selectpicker();
  var medicalcollegelistValue;
  $(document).on("change", "#medicalcollegelist", function () {
    medicalcollegelistValue = $("#medicalcollegelist").val();
   
    load_data_area(medicalcollegelistValue);
  });

  function load_data_area( medicalcollegelistValue) {
      $.ajax({
          url: "/cameraArea",
          method: "POST",
          data: {medicalcollegelistValue},
          dataType: "json",
          success: function (data) { 
            
            var html = "";

            coll=data[0]
                      for (var count = 0; count < coll.length; count++) {
                        
                          html += '<option value="' + coll[count] + '">' + coll[count] + "</option>";
                      } 
                    

                          $("#CameraLocationArea").html(html);
                          
                          $("#CameraLocationArea").selectpicker("refresh");
                      
                  },
              });
            }

              $(document).on("change", "#CameraLocationArea", function () {
                var CameraLocationAreaValue =  $("#CameraLocationArea").val();
                console.log(CameraLocationAreaValue)
               
                load_data_subarea(CameraLocationAreaValue);
              });
              
              function load_data_subarea( CameraLocationAreaValue) {
                $.ajax({
                    url: "/cameraSubArea",
                    method: "POST",
                    data: {medicalcollegelistValue,CameraLocationAreaValue},
                    dataType: "json",
                    success: function (data) { 

                      var html = "";
                      coll=data[0]
                                for (var count = 0; count < coll.length; count++) {
                                 
                                    html += '<option value="' + coll[count] + '">' + coll[count] + "</option>";
                                } 
                              
    
                                    $("#CameraLocationSubArea").html(html);
                                    
                                    $("#CameraLocationSubArea").selectpicker("refresh");
                                
                            },
                        });
                      }
 
});
