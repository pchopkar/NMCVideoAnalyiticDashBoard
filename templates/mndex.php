<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
    <!-- <link rel="stylesheet" href="main.css"> -->
    <script type="text/JavaScript">
      function showMessage(){
          var message = document.getElementById("message").value;
          display_message.innerHTML= message;
      }
  </script>

    <TITLE>NMC Video Analytic DashBoard</TITLE>
  </head>
  <body>
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.3/dist/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>

    <div class="col-md-6 offset-md-3 mt-5">
    
         <h1 >NMC Video Analytic DashBoard</h1>
         <br>
         <form accept-charset="UTF-8" action="count" method="POST" enctype="multipart/form-data" target="_blank">
           <!-- <div class="form-group">
             <label for="exampleInputName">Full Name</label>
            <select class="form-control" id="exampleFormControlSelect1" name="platform" required="required">
               <option>Github</option>
               <option>Gitlab</option>
               <option>Bitbucket</option>
             </select>
           </div>
           <div class="form-group">
             <label for="exampleInputEmail1" required="required">Email address</label>
             <select class="form-control" id="exampleFormControlSelect1" name="platform" required="required">
                <option>Github</option>
                <option>Gitlab</option>
                <option>Bitbucket</option>
              </select>
           </div> -->
           <div class="form-group">
            <label for="exampleFormControlSelect1">Medicle College</label>
            <select class="form-control" id="exampleFormControlSelect1" name="Medicle College" required="required">
              <option selected>--SELECT--</option>
              <option value="Delhi Medicle College">Delhi Medicle College</option>
              <option value="Nagpur Medicle College">Nagpur Medicle College</option>
              <option value="Maharashtra Medicle College">Maharashtra Medicle College</option>
              <option value="Punjab Medicle College">Punjab Medicle College</option>
            </select>
            <br>
             <label for="exampleFormControlSelect1">Camera Location</label>
             <select class="form-control" id="exampleFormControlSelect1" name="Camera Location" required="required">
               <option selected>--SELECT--</option>
               <option value="OPD">OPD</option>
               <option value ="DepartMent">DepartMent</option>
               <option value="Lecture Hall">Lecture Hall</option>
               <option value="Lab Area">Lab Area</option>
             </select>
             <br>
             <label for="exampleFormControlSelect1">Date and Time :&nbsp;&nbsp;   
              <input type="datetime-local" id="Test_DatetimeLocal" name="Date and Time">
            </label>

           </div>
           <hr>
           <!-- <div class="frame"> -->
            <!-- <div class="center"> -->
                <div class="title">
                    <label for="exampleInputName">Upload a file</label>
                </div>
        
                <div class="dropzone">
                    <!-- <img src="http://100dayscss.com/codepen/upload.svg" class="upload-icon" /> -->
                    <input type="file" class="upload-input" />
                </div>
        
                <!-- <button type="button" class="btn" name="uploadbutton">Upload file</button> -->
    
                <!-- <br>
                <button on type="submit" class="btn btn-primary">Upload file</button> -->
        
            <!-- </div> -->
            <hr>
            <button type="submit" class="btn btn-primary">Submit</button>
        </div>
        
        <!-- original pen: https://codepen.io/roydigerhund/pen/ZQdbeN  -->
        <!-- NO JS ADDED YET -->
           <!-- <div class="form-group mt-3">
             <label class="mr-2">Upload your CV:</label>
             <input type="file" name="file">
           </div> -->

         </form>
  </body>
</html>

