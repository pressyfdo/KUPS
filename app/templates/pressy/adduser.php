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
					
				<label for="username" class="control-label col-xs-2"> username</label>
					<div class="col-xs-10">
						<input type="text" class="form-control" id="username" placeholder="username">
						</br>
					</div>
					
				<label for="Email" class="control-label col-xs-2">Email</label>
					<div class="col-xs-10">
						<input type="text" class="form-control" id="email" placeholder="email">
						</br>
					</div>				
			
			
				<label for="Role" class="control-label col-xs-2"> role</label>
					<div class="col-xs-10">
						<select class="form-control">
							<option>Admin</option>
							<option>user</option>
						</select> 
						</br>
						
				<label for="Mobile" class="control-label col-xs-2"> Mobile</label>
					<div class="col-xs-10">
						<input type="Number" class="form-control" id="mobile" placeholder="mobile">
						</br>
					</div>	
				
				
					
				<button type="submit" class="btn btn-lg btn-primary ">Register <span class="glyphicon glyphicon-print" aria-hidden="true"></button>				
			
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
