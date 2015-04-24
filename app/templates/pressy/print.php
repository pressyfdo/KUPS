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
        
        <div>
			<table class="table table-striped">
		<tr>
			<th>S.no </th>
			<th>Printer name </th>
			<th>Department </th>
			<th>Location </th>
			<th>Description</th>
			<th>&nbsp;</th>
		</tr>
		<tr><td>1</td>
		<td>certificate.pdf</td>
		<td>Cse</td>
		<td>Karunya</td>
		<td>for interview</td>
				 '<td>
						<a href='.$this->url('witness',
							array('action'=>'edit', 'id' => $wit->witness_id)).'> <span class="glyphicon glyphicon-pencil" aria-hidden="true"></span> Edit</a>
						&nbsp; &nbsp; | &nbsp; &nbsp; 
						<a href='.$this->url('witness',
							array('action'=>'delete', 'id' => $wit->witness_id)).'> <span class="glyphicon glyphicon-remove" aria-hidden="true"></span> Delete</a>
					</td></tr>;
		
		</table>
        
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
