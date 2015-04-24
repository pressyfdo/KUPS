<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Kups</title>
    
    <!-- Bootstrap -->
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="evitrack.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="justified-nav.css" rel="stylesheet">
    
  </head>
  <body>
	   <div class="container">

      <div class="masthead">
		  
			<div class="btn-group pull-right">
			  <button type="button" class="btn btn-default"><span class="glyphicon glyphicon-user" aria-hidden="true"></span> User </button>
			  <button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown" aria-expanded="false">
				<span class="caret"></span>
				<span class="sr-only">Toggle Dropdown</span>
			  </button>
			  <ul class="dropdown-menu" role="menu">
				<li><a href="#">Action</a></li>
				<li><a href="#">Another action</a></li>
				<li><a href="#">Something else here</a></li>
			  </ul>
			</div>
			
			<h1 class="text-muted">Kups</h1> 
		
        <nav>
          <ul class="nav nav-justified">
            <li class="active"><a href="index.php">Home <span class="glyphicon glyphicon-home" aria-hidden="true"></span></a></li>
            <li><a href="print.php">Printers <span class="glyphicon glyphicon-print" aria-hidden="true"></span></a></li>
            <li><a href="jobs.php">Jobs <span class="glyphicon glyphicon-usd" aria-hidden="true"></span></a></li>
            <li><a href="search.php">Uploads <span class="glyphicon glyphicon-upload" aria-hidden="true"></span></a></li>
           
            
          </ul>
        </nav>
        </br>
        </br>
        
        <div class="row marketing">
	    <div class="col-md-10 col-sm-12 col-lg-7" >
        <div class="col-md-8 box-images">
			  
			  <img src="wolf.png" alt="wolf" class="img-thumbnail">
			  <img src="wolf.png" alt="wolf" class="img-thumbnail">
			  <img src="wolf.png" alt="wolf" class="img-thumbnail">
			  <img src="wolf.png" alt="wolf" class="img-thumbnail">
			  <img src="wolf.png" alt="wolf" class="img-thumbnail">
			  
		 </div>
		  </br>
		  <div class="form-group">
			<label for="exampleInputFile"></label>
			<input type="file" id="exampleInputFile">
			<button type="submit" class="btn btn-lg btn-primary pull-right">Upload <span class="glyphicon glyphicon-upload" aria-hidden="true"></button>
			</div>	
        </div>
        
        <div class="col-md-4 col-sm-12 col-lg-5 ">
			<form class="form-horizontal">
				<div class="form-group">
					
					<label for="pages" class="control-label col-xs-2"> Pages</label>
					<div class="col-xs-10">
						<div class="radio">
						  <label><input type="radio" name="pages">All</label>
						</div>
						<div class="radio">
						  <label><input type="radio" name="pages"><input type="text" class="form-control" id="radio-input" placeholder="eg: 1-5, 8, 4"></label>
						</div>
						</br>
					</div>
					
					<label for="copies" class="control-label col-xs-2"> Copies</label>
					<div class="col-xs-10">
						<input type="number" class="form-control" id="copies" placeholder="Specify Copies">
						</br>
					</div>
					
					</br>
					
					<label for="Layout" class="control-label col-xs-2"> layout</label>
					<div class="col-xs-10">
						<select class="form-control">
							<option>portrait</option>
							<option>Landscape</option>
						</select> 
						</br>
					</div>
					
					<label for="Page-size" class="control-label col-xs-2"> Page size</label>
					<div class="col-xs-10">
						<select class="form-control">
							<option>A4</option>
							<option>A3</option>
							<option>Letter</option>
							<option>Legal</option>
						</select> 
						</br>
					</div>
					
					<label for="Printer" class="control-label col-xs-2"> Printer</label>
					<div class="col-xs-10">
						<select class="form-control">
							<option>Printer 1</option>
							<option>Printer 2</option>
							<option>Printer 3</option>
							<option>Printer 4</option>
						</select> 
					</br>
					</div>
					
					<label for="Side" class="control-label col-xs-2"> Side</label>
					<div class="col-xs-10">
						<select class="form-control">
							<option>Single</option>
							<option>Double side</option>
						</select> 
					</br></br>
					</div>
					
					<center>
					<button type="submit" class="btn btn-lg btn-primary ">print <span class="glyphicon glyphicon-print" aria-hidden="true"></button>
					</center>
				</div>
			</form>
		</div>
		</div>
	  <center>
      <footer class="footer">
        <p>&copy; Tharun 2014</p>
      </footer>
      </center>
    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="js/bootstrap.min.js"></script>
    
  </body>
</html>
