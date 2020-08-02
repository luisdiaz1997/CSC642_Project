<!DOCTYPE html>
<html lang="en">
<body style="background-color:orange;">

<head>
    <title>SFSU Software Engineering Project CSC 642, Summer 2020. For Demonstration Only</title>
    <!-- Bootstrap -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <!-- Bootstrap Validator -->
    <link rel="stylesheet" href="http://cdnjs.cloudflare.com/ajax/libs/jquery.bootstrapvalidator/0.5.3/css/bootstrapValidator.min.css" />
    <script type="text/javascript" src="http://cdnjs.cloudflare.com/ajax/libs/jquery.bootstrapvalidator/0.5.3/js/bootstrapValidator.min.js">
    </script>
    <!-- Google Recaptcha -->
    <script src='https://www.google.com/recaptcha/api.js'></script>
    <!-- Google Fonts -->
    <link href='http://fonts.googleapis.com/css?family=Nunito' rel='stylesheet' type='text/css'>
    <!-- Google Maps API -->
    <script src="https://maps.googleapis.com/maps/api/js"></script>
    <!-- Custom Stylesheet -->
    <link href="stylesheet.css" rel="stylesheet">
</head>

<?php include 'navbar.html'; ?>

<body>
<br>
<center>
    <h1>Welcome to Fooridise's Reigstration Form. Your Food awaits you!</h1>
    <br>
    <br> Please fill out your information below:
</center>
<br>
<div class="container center-div">
    <div class="container jumbotron jumbotron-fluid" id="main-container">
        <div class="container center-div">
            <div class="col-lg-12">
                <form id="registrationForm" method="post" action="indi_verification.php" data-toggle="validator">
                    <div class="row">
                        <div class="wrapper">
                            <div class="form-group col-md-5 has-feedback">
                                <label for="firstName">First Name</label>
                                <input type="text" class="form-control" id="firstName" placeholder="First name" name="firstName" pattern="[a-zA-Z]+" required>
                            </div>
                        </div>
                        <div class="wrapper">
                            <div class="form-group col-md-5 has-feedback">
                                <label for="lastName">Last Name</label>
                                <input type="text" class="form-control" id="lastName" placeholder="Last name" name="lastName" pattern="[a-zA-Z]+" required>
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="wrapper">
                            <div class="form-group col-md-10">
                                <label for="address">Address</label>
                                <input type="text" class="form-control" id="address" placeholder="1600 Holloway Ave, San Francisco, CA 94132" name="address" pattern="[a-zA-Z0-9]+" required>
                            </div>
                        </div>
                    </div>
                    <br>
                    <div class="row">
                        <div class="wrapper">
                            <div class="form-group col-md-7">
                                <label for="education">Are you a SFSU Student?</label>
                                <select name="education" id="education" class="form-control">
                                    <option value="">Choose One</option>
                                    <option>Yes</option>
                                    <option>No</option>
                                </select>
                            </div>
                        </div>
                    </div>
                    <br>
                    <div class="row">
                        <div class="wrapper">
                            <div class="form-group col-md-5">
                                <label for="phone">Phone</label>
                                <input type="text" class="form-control" id="phone" placeholder="4153246789" name="phone" pattern="[0-9]{10}" required>
                                <p class="form-text text-muted">
                                <h5>
                                    Your phone number must contain 10 digits.
                                </h5>
                                </p>
                            </div>
                        </div>
                        <div class="wrapper">
                            <div class="form-group col-md-7">
                                <label for="email">E-mail</label>
                                <input type="email" class="form-control" id="email" placeholder="user@mail.sfsu.edu" name="email">
                            </div>
                        </div>
                    </div>
                    <br>
                    <div class="row">
                        <div class="wrapper">
                            <div class="form-group col-md-6 has-feedback">
                                <label for="password">Password</label>
                                <input type="password" class="form-control" id="password" name="password" pattern="[a-zA-Z0-9]+" required>
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="wrapper">
                            <div class="form-group col-md-6">
                                <label for="passwordConfirmation">Confirm Password</label>
                                <input type="password" class="form-control" id="passwordConfirmation" name="passwordConfirmation">
                            </div>
                        </div>
                    </div>
                    <br>
                    <div class="form-group">
                        <div class="wrapper2">
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" id="terms" name="terms"> I agree to the <a href="FormAux.html" target="_blank">terms and conditions.</a>
                            </div>
                        </div>
                    </div>
                    <br>
                    <div class="row">
                        <div class="wrapper">
                            <div class="form-group col-md-6">
                                <div class="g-recaptcha" data-sitekey="6Lf6kLIZAAAAALC22EX4M4oBxDR-SZWhnxu6dm-A"></div>

                            </div>
                        </div>
                    </div>
                    <br>
                    <br>
                    <br>
                    <div class="row">
                        <button type="submit" class="btn btn-success" style="float: right;">REGISTER</button>
                        <button type="reset" class="btn btn-default" style="float: left;">CANCEL</button>
                    </div>
                    <h5>
                        <a href="FormAux.html" target="_blank" style="float: right;">       Forgot your password?</a>
                    </h5>
                </form>
            </div>
        </div>
    </div>
</div>
<br>
<br>
<script type="text/javascript">
    // (Field validations: first  and last name up to 40 characters; phone - 7 positive digits;, address – each entry up to 40 alpha numeric characters; Zip code- positive 5 digit number).
    $(document).ready(function() {
        $('#registrationForm').bootstrapValidator({
            feedbackIcons: {
                valid: 'glyphicon glyphicon-ok',
                invalid: 'glyphicon glyphicon-remove',
                validating: 'glyphicon glyphicon-refresh'
            },
            fields: {
                firstName: {
                    validators: {
                        stringLength: {
                            max: 40
                        },
                        notEmpty: {
                            message: 'Please type your first name.'
                        }

                    }
                },
                lastName: {
                    validators: {
                        stringLength: {
                            max: 40
                        },
                        notEmpty: {
                            message: 'Please type your last name.'
                        }
                    }
                },
                address: {
                    validators: {
                        stringLength: {
                            max: 200
                        },
                        notEmpty: {
                            message: 'Please type your address.'
                        }
                    }
                },
                education: {
                    validators: {
                        notEmpty: {
                            message: 'Please select your educational level.'
                        }
                    }
                },
                income: {
                    validators: {
                        notEmpty: {
                            message: 'Please select your income.'
                        }
                    }
                },
                phone: {
                    validators: {
                        numeric: {
                            message: 'This field should contain a number.'
                        },
                        notEmpty: {
                            message: 'Please type your phone number.'
                        }
                    }
                },
                email: {
                    validators: {
                        notEmpty: {
                            message: 'Please type your E-mail.'
                        },
                        emailAddress: {
                            message: 'Please enter a valid email address.'
                        }
                    }
                },
                password: {
                    validators: {
                        notEmpty: {
                            message: 'Please type in a password.'
                        }
                    }
                },
                passwordConfirmation: {
                    validators: {
                        notEmpty: {
                            message: 'Make sure the passwords are identical.'
                        },
                        identical: {
                            field: 'password',
                            message: 'Passwords do not match.'
                        }
                    }
                },
                terms: {
                    validators: {
                        notEmpty: {
                            message: 'Please agree to the terms and conditions.'
                        }
                    }
                },
            }
        })
    });
</script>

</body>
<?php include 'footer.php'; ?>

</html>