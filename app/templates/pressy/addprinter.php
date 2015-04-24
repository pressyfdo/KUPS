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
            <li ><a href="index.php">Home <span class="glyphicon glyphicon-home" aria-hidden="true"></span></a></li>
            <li class="active"><a href="print.php">Printers <span class="glyphicon glyphicon-print" aria-hidden="true"></span></a></li>
            <li><a href="jobs.php">Jobs <span class="glyphicon glyphicon-usd" aria-hidden="true"></span></a></li>
            <li><a href="search.php">Uploads <span class="glyphicon glyphicon-upload" aria-hidden="true"></span></a></li>
           
            
          </ul>
        </nav>
        </br>
        </br>
        
        
		<div class="form-group">	
			
			
				<label for="Name" class="control-label col-xs-2"> Name</label>
					<div class="col-xs-10">
						<input type="text" class="form-control" id="name" placeholder="Name">
						</br>
					</div>
					
				<label for="URl" class="control-label col-xs-2"> URL</label>
					<div class="col-xs-10">
						<input type="text" class="form-control" id="url" placeholder="URL">
						</br>
					</div>
					
				<label for="Model" class="control-label col-xs-2"> Model</label>
					<div class="col-xs-10">
						<input type="text" class="form-control" id="model" placeholder="model">
						</br>
					</div>				
			
			
				<label for="Department" class="control-label col-xs-2"> Department</label>
					<div class="col-xs-10">
						<select class="form-control">
							<option>portrait</option>
							<option>Landscape</option>
						</select> 
						</br>
						
				<label for="Location" class="control-label col-xs-2"> Location</label>
					<div class="col-xs-10">
						<input type="text" class="form-control" id="Location" placeholder="Location">
						</br>
					</div>	
				
				<label for="Description" class="control-label col-xs-2"> Description</label>
					<div class="col-xs-10">
						<input type="text-area" class="form-control" id="desc" placeholder="Description">
						</br>
					</div>	
					
				<button type="submit" class="btn btn-lg btn-primary ">Add <span class="glyphicon glyphicon-print" aria-hidden="true"></button>				
			
		</div>
		
        
        </form>
        
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
