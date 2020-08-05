<!DOCTYPE HTML>
<html>
<body style="background-color:orange;">

<head>

    <title>SFSU Software Engineering Project CSC 642, Summer 2020. For Demonstration Only</title>
    <!-- Bootstrap -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <!-- Google Fonts -->
    <link href='http://fonts.googleapis.com/css?family=Nunito' rel='stylesheet' type='text/css'>
    <!-- Custom Stylesheet -->
    <link href="stylesheet.css" rel="stylesheet" type="text/css">

</head>

<?php include 'navbar.html'; ?>

<body>

<center><h1>Welcome to Fooridise!</h1></center>
<br>
<div class="container center-div">
    <div class="container jumbotron jumbotron-fluid" id="main-container">
        <div class="container center-div">
            <h2>Welcome <?php echo $_POST["firstName"]; ?>,</h2><h3> ... here is the information you entered: </h3><br>
            <div class="row">
                <div class="col-md-5">
                    <div class="row"><b>Full Name:</b> <?php echo $_POST["firstName"]; ?> <?php echo $_POST["lastName"]; ?></div><br>
                    <div class="row"><b>Address:</b> <?php echo $_POST["address"]; ?></div><br>
                    <div class="row"><b>SFSU Student:</b> <?php echo $_POST["education"]; ?></div><br>
                    <div class="row"><b>Phone:</b> <?php echo $_POST["phone"]; ?></div><br>
                    <div class="row"><b>E-mail:</b> <?php echo $_POST["email"]; ?></div><br>
                    <div class="row"><b>Password:</b> <?php echo $_POST["password"]; ?></div></div>

            </div>
        </div><br><br><br><br>
    </div></div>

</body>
<?php include 'footer.php'; ?>

</html>