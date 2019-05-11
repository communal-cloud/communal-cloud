<template>
    <div class="kt-portlet kt-portlet--height-fluid">
        <div class="kt-portlet__head">
            <div class="kt-portlet__head-label">
                <h3 class="kt-portlet__head-title">
                    Create Community
                </h3>
            </div>
        </div>
        <div class="kt-portlet__body kt-portlet__body--fluid">
            <div class="kt-grid  kt-wizard-v1 kt-wizard-v1--white" id="kt_wizard_v1" data-ktwizard-state="first">
                <div class="kt-grid__item">
                    <!--begin: Form Wizard Nav -->
                    <div class="kt-wizard-v1__nav">
                        <div class="kt-wizard-v1__nav-items">
                            <a class="kt-wizard-v1__nav-item" href="#" data-ktwizard-type="step" data-ktwizard-state="current">
                                <div class="kt-wizard-v1__nav-body">
                                    <div class="kt-wizard-v1__nav-icon">
                                        <i class="flaticon-bus-stop"></i>
                                    </div>
                                    <div class="kt-wizard-v1__nav-label">
                                        1) Create Community
                                    </div>
                                </div>
                            </a>
                            <a class="kt-wizard-v1__nav-item" href="#" data-ktwizard-type="step" data-ktwizard-state="pending">
                                <div class="kt-wizard-v1__nav-body">
                                    <div class="kt-wizard-v1__nav-icon">
                                        <i class="flaticon-list"></i>
                                    </div>
                                    <div class="kt-wizard-v1__nav-label">
                                        2) Enter Details
                                    </div>
                                </div>
                            </a>
                            <a class="kt-wizard-v1__nav-item" href="#" data-ktwizard-type="step" data-ktwizard-state="pending">
                                <div class="kt-wizard-v1__nav-body">
                                    <div class="kt-wizard-v1__nav-icon">
                                        <i class="flaticon-responsive"></i>
                                    </div>
                                    <div class="kt-wizard-v1__nav-label">
                                        3) Select Services
                                    </div>
                                </div>
                            </a>
                            <a class="kt-wizard-v1__nav-item" href="#" data-ktwizard-type="step" data-ktwizard-state="pending">
                                <div class="kt-wizard-v1__nav-body">
                                    <div class="kt-wizard-v1__nav-icon">
                                        <i class="flaticon-truck"></i>
                                    </div>
                                    <div class="kt-wizard-v1__nav-label">
                                        4) Delivery Address
                                    </div>
                                </div>
                            </a>
                            <a class="kt-wizard-v1__nav-item" href="#" data-ktwizard-type="step" data-ktwizard-state="pending">
                                <div class="kt-wizard-v1__nav-body">
                                    <div class="kt-wizard-v1__nav-icon">
                                        <i class="flaticon-globe"></i>
                                    </div>
                                    <div class="kt-wizard-v1__nav-label">
                                        5) Review and Submit
                                    </div>
                                </div>
                            </a>
                        </div>
                    </div>
                    <!--end: Form Wizard Nav -->

                </div>
                <div class="kt-grid__item kt-grid__item--fluid kt-wizard-v1__wrapper">
                    <!--begin: Form Wizard Form-->
                    <form class="kt-form" id="kt_form" novalidate="novalidate">
                        <!--begin: Form Wizard Step 1-->
                        <div class="kt-wizard-v1__content" data-ktwizard-type="step-content" data-ktwizard-state="current">
                            <div class="kt-heading kt-heading--md">Setup Your Current Location</div>
                            <div class="kt-form__section kt-form__section--first">
                                <div class="kt-wizard-v1__form">
                                    <div class="form-group">
                                        <label>Address Line 1</label>
                                        <input type="text" class="form-control" name="address1" placeholder="Address Line 1" value="Address Line 1">
                                        <span class="form-text text-muted">Please enter your Address.</span>
                                    </div>
                                    <div class="form-group">
                                        <label>Address Line 2</label>
                                        <input type="text" class="form-control" name="address2" placeholder="Address Line 2" value="Address Line 2">
                                        <span class="form-text text-muted">Please enter your Address.</span>
                                    </div>
                                    <div class="row">
                                        <div class="col-xl-6">
                                            <div class="form-group">
                                                <label>Postcode</label>
                                                <input type="text" class="form-control" name="postcode" placeholder="Postcode" value="3000">
                                                <span class="form-text text-muted">Please enter your Postcode.</span>
                                            </div>
                                        </div>
                                        <div class="col-xl-6">
                                            <div class="form-group">
                                                <label>City</label>
                                                <input type="text" class="form-control" name="city" placeholder="City" value="Melbourne">
                                                <span class="form-text text-muted">Please enter your City.</span>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-xl-6">
                                            <div class="form-group">
                                                <label>State</label>
                                                <input type="text" class="form-control" name="state" placeholder="State" value="VIC">
                                                <span class="form-text text-muted">Please enter your Postcode.</span>
                                            </div>
                                        </div>
                                        <div class="col-xl-6">
                                            <div class="form-group">
                                                <label>Country:</label>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!--end: Form Wizard Step 1-->

                        <!--begin: Form Wizard Step 2-->
                        <div class="kt-wizard-v1__content" data-ktwizard-type="step-content">
                            <div class="kt-heading kt-heading--md">Enter the Details of your Delivery</div>
                            <div class="kt-form__section kt-form__section--first">
                                <div class="kt-wizard-v1__form">
                                    <b-input-group
                                            prepend="Name"
                                            class="mt-3"
                                            id="name"
                                            description="name of the community"
                                            label="Enter a community name"
                                            label-for="name"

                                    >
                                        <b-form-input v-model="community_name" type="text"/>

                                    </b-input-group>
                                    <b-input-group
                                            prepend="Purpose"
                                            class="mt-3"
                                            id="purpose"
                                            label="Purpose"
                                            label-for="purpose"

                                    >
                                        <b-form-input v-model="community_purpose" type="text" />
                                    </b-input-group>

                                    <b-input-group
                                            prepend="Categories"
                                            class="mt-3"
                                            id="categories"
                                            label="Categories"
                                            label-for="categories"

                                    >
                                        <b-form-input v-model="community_category" type="text" />
                                        <b-input-group-append>
                                            <b-button v-on:click="AddCategory" variant="outline-success">Add</b-button>
                                        </b-input-group-append>
                                    </b-input-group>

                                    <ul id="categories">
                                        <li v-for="category in community_categories" :key="category">
                                            <b-button v-on:click="RemoveCategory(category)">{{ category }}</b-button>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                        <!--end: Form Wizard Step 2-->

                        <!--begin: Form Wizard Step 3-->
                        <div class="kt-wizard-v1__content" data-ktwizard-type="step-content">
                            <div class="kt-heading kt-heading--md">Select your Services</div>
                            <div class="kt-form__section kt-form__section--first">
                                <div class="kt-wizard-v1__form">
                                    <div class="form-group">
                                        <label>Delivery Type</label>
                                        <select name="delivery" class="form-control">
                                            <option value="">Select a Service Type Option</option>
                                            <option value="overnight" selected="">Overnight Delivery (within 48 hours)</option>
                                            <option value="express">Express Delivery (within 5 working days)</option>
                                            <option value="basic">Basic Delivery (within 5 - 10 working days)</option>
                                        </select>
                                    </div>
                                    <div class="form-group">
                                        <label>Packaging Type</label>
                                        <select name="packaging" class="form-control">
                                            <option value="">Select a Packaging Type Option</option>
                                            <option value="regular" selected="">Regular Packaging</option>
                                            <option value="oversized">Oversized Packaging</option>
                                            <option value="fragile">Fragile Packaging</option>
                                            <option value="frozen">Frozen Packaging</option>
                                        </select>
                                    </div>
                                    <div class="form-group">
                                        <label>Preferred Delivery Window</label>
                                        <select name="preferreddelivery" class="form-control">
                                            <option value="">Select a Preferred Delivery Option</option>
                                            <option value="morning" selected="">Morning Delivery (8:00AM - 11:00AM)</option>
                                            <option value="afternoon">Afternoon Delivery (11:00AM - 3:00PM)</option>
                                            <option value="evening">Evening Delivery (3:00PM - 7:00PM)</option>
                                        </select>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!--end: Form Wizard Step 3-->

                        <!--begin: Form Wizard Step 4-->
                        <div class="kt-wizard-v1__content" data-ktwizard-type="step-content">
                            <div class="kt-heading kt-heading--md">Setup Your Delivery Location</div>
                            <div class="kt-form__section kt-form__section--first">
                                <div class="kt-wizard-v1__form">
                                    <div class="form-group">
                                        <label>Address Line 1</label>
                                        <input type="text" class="form-control" name="locaddress1" placeholder="Address Line 1" value="Address Line 1">
                                        <span class="form-text text-muted">Please enter your Address.</span>
                                    </div>
                                    <div class="form-group">
                                        <label>Address Line 2</label>
                                        <input type="text" class="form-control" name="locaddress2" placeholder="Address Line 2" value="Address Line 2">
                                        <span class="form-text text-muted">Please enter your Address.</span>
                                    </div>
                                    <div class="row">
                                        <div class="col-xl-6">
                                            <div class="form-group">
                                                <label>Postcode</label>
                                                <input type="text" class="form-control" name="locpostcode" placeholder="Postcode" value="3072">
                                                <span class="form-text text-muted">Please enter your Postcode.</span>
                                            </div>
                                        </div>
                                        <div class="col-xl-6">
                                            <div class="form-group">
                                                <label>City</label>
                                                <input type="text" class="form-control" name="loccity" placeholder="City" value="Preston">
                                                <span class="form-text text-muted">Please enter your City.</span>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-xl-6">
                                            <div class="form-group">
                                                <label>State</label>
                                                <input type="text" class="form-control" name="locstate" placeholder="State" value="VIC">
                                                <span class="form-text text-muted">Please enter your Postcode.</span>
                                            </div>
                                        </div>
                                        <div class="col-xl-6">
                                            <div class="form-group">
                                                <label>Country:</label>
                                                <select name="loccountry" class="form-control">
                                                    <option value="">Select</option>
                                                    <option value="AF">Afghanistan</option>
                                                    <option value="AX">Åland Islands</option>
                                                    <option value="AL">Albania</option>
                                                    <option value="DZ">Algeria</option>
                                                    <option value="AS">American Samoa</option>
                                                    <option value="AD">Andorra</option>
                                                    <option value="AO">Angola</option>
                                                    <option value="AI">Anguilla</option>
                                                    <option value="AQ">Antarctica</option>
                                                    <option value="AG">Antigua and Barbuda</option>
                                                    <option value="AR">Argentina</option>
                                                    <option value="AM">Armenia</option>
                                                    <option value="AW">Aruba</option>
                                                    <option value="AU" selected="">Australia</option>
                                                    <option value="AT">Austria</option>
                                                    <option value="AZ">Azerbaijan</option>
                                                    <option value="BS">Bahamas</option>
                                                    <option value="BH">Bahrain</option>
                                                    <option value="BD">Bangladesh</option>
                                                    <option value="BB">Barbados</option>
                                                    <option value="BY">Belarus</option>
                                                    <option value="BE">Belgium</option>
                                                    <option value="BZ">Belize</option>
                                                    <option value="BJ">Benin</option>
                                                    <option value="BM">Bermuda</option>
                                                    <option value="BT">Bhutan</option>
                                                    <option value="BO">Bolivia, Plurinational State of</option>
                                                    <option value="BQ">Bonaire, Sint Eustatius and Saba</option>
                                                    <option value="BA">Bosnia and Herzegovina</option>
                                                    <option value="BW">Botswana</option>
                                                    <option value="BV">Bouvet Island</option>
                                                    <option value="BR">Brazil</option>
                                                    <option value="IO">British Indian Ocean Territory</option>
                                                    <option value="BN">Brunei Darussalam</option>
                                                    <option value="BG">Bulgaria</option>
                                                    <option value="BF">Burkina Faso</option>
                                                    <option value="BI">Burundi</option>
                                                    <option value="KH">Cambodia</option>
                                                    <option value="CM">Cameroon</option>
                                                    <option value="CA">Canada</option>
                                                    <option value="CV">Cape Verde</option>
                                                    <option value="KY">Cayman Islands</option>
                                                    <option value="CF">Central African Republic</option>
                                                    <option value="TD">Chad</option>
                                                    <option value="CL">Chile</option>
                                                    <option value="CN">China</option>
                                                    <option value="CX">Christmas Island</option>
                                                    <option value="CC">Cocos (Keeling) Islands</option>
                                                    <option value="CO">Colombia</option>
                                                    <option value="KM">Comoros</option>
                                                    <option value="CG">Congo</option>
                                                    <option value="CD">Congo, the Democratic Republic of the</option>
                                                    <option value="CK">Cook Islands</option>
                                                    <option value="CR">Costa Rica</option>
                                                    <option value="CI">Côte d'Ivoire</option>
                                                    <option value="HR">Croatia</option>
                                                    <option value="CU">Cuba</option>
                                                    <option value="CW">Curaçao</option>
                                                    <option value="CY">Cyprus</option>
                                                    <option value="CZ">Czech Republic</option>
                                                    <option value="DK">Denmark</option>
                                                    <option value="DJ">Djibouti</option>
                                                    <option value="DM">Dominica</option>
                                                    <option value="DO">Dominican Republic</option>
                                                    <option value="EC">Ecuador</option>
                                                    <option value="EG">Egypt</option>
                                                    <option value="SV">El Salvador</option>
                                                    <option value="GQ">Equatorial Guinea</option>
                                                    <option value="ER">Eritrea</option>
                                                    <option value="EE">Estonia</option>
                                                    <option value="ET">Ethiopia</option>
                                                    <option value="FK">Falkland Islands (Malvinas)</option>
                                                    <option value="FO">Faroe Islands</option>
                                                    <option value="FJ">Fiji</option>
                                                    <option value="FI">Finland</option>
                                                    <option value="FR">France</option>
                                                    <option value="GF">French Guiana</option>
                                                    <option value="PF">French Polynesia</option>
                                                    <option value="TF">French Southern Territories</option>
                                                    <option value="GA">Gabon</option>
                                                    <option value="GM">Gambia</option>
                                                    <option value="GE">Georgia</option>
                                                    <option value="DE">Germany</option>
                                                    <option value="GH">Ghana</option>
                                                    <option value="GI">Gibraltar</option>
                                                    <option value="GR">Greece</option>
                                                    <option value="GL">Greenland</option>
                                                    <option value="GD">Grenada</option>
                                                    <option value="GP">Guadeloupe</option>
                                                    <option value="GU">Guam</option>
                                                    <option value="GT">Guatemala</option>
                                                    <option value="GG">Guernsey</option>
                                                    <option value="GN">Guinea</option>
                                                    <option value="GW">Guinea-Bissau</option>
                                                    <option value="GY">Guyana</option>
                                                    <option value="HT">Haiti</option>
                                                    <option value="HM">Heard Island and McDonald Islands</option>
                                                    <option value="VA">Holy See (Vatican City State)</option>
                                                    <option value="HN">Honduras</option>
                                                    <option value="HK">Hong Kong</option>
                                                    <option value="HU">Hungary</option>
                                                    <option value="IS">Iceland</option>
                                                    <option value="IN">India</option>
                                                    <option value="ID">Indonesia</option>
                                                    <option value="IR">Iran, Islamic Republic of</option>
                                                    <option value="IQ">Iraq</option>
                                                    <option value="IE">Ireland</option>
                                                    <option value="IM">Isle of Man</option>
                                                    <option value="IL">Israel</option>
                                                    <option value="IT">Italy</option>
                                                    <option value="JM">Jamaica</option>
                                                    <option value="JP">Japan</option>
                                                    <option value="JE">Jersey</option>
                                                    <option value="JO">Jordan</option>
                                                    <option value="KZ">Kazakhstan</option>
                                                    <option value="KE">Kenya</option>
                                                    <option value="KI">Kiribati</option>
                                                    <option value="KP">Korea, Democratic People's Republic of</option>
                                                    <option value="KR">Korea, Republic of</option>
                                                    <option value="KW">Kuwait</option>
                                                    <option value="KG">Kyrgyzstan</option>
                                                    <option value="LA">Lao People's Democratic Republic</option>
                                                    <option value="LV">Latvia</option>
                                                    <option value="LB">Lebanon</option>
                                                    <option value="LS">Lesotho</option>
                                                    <option value="LR">Liberia</option>
                                                    <option value="LY">Libya</option>
                                                    <option value="LI">Liechtenstein</option>
                                                    <option value="LT">Lithuania</option>
                                                    <option value="LU">Luxembourg</option>
                                                    <option value="MO">Macao</option>
                                                    <option value="MK">Macedonia, the former Yugoslav Republic of</option>
                                                    <option value="MG">Madagascar</option>
                                                    <option value="MW">Malawi</option>
                                                    <option value="MY">Malaysia</option>
                                                    <option value="MV">Maldives</option>
                                                    <option value="ML">Mali</option>
                                                    <option value="MT">Malta</option>
                                                    <option value="MH">Marshall Islands</option>
                                                    <option value="MQ">Martinique</option>
                                                    <option value="MR">Mauritania</option>
                                                    <option value="MU">Mauritius</option>
                                                    <option value="YT">Mayotte</option>
                                                    <option value="MX">Mexico</option>
                                                    <option value="FM">Micronesia, Federated States of</option>
                                                    <option value="MD">Moldova, Republic of</option>
                                                    <option value="MC">Monaco</option>
                                                    <option value="MN">Mongolia</option>
                                                    <option value="ME">Montenegro</option>
                                                    <option value="MS">Montserrat</option>
                                                    <option value="MA">Morocco</option>
                                                    <option value="MZ">Mozambique</option>
                                                    <option value="MM">Myanmar</option>
                                                    <option value="NA">Namibia</option>
                                                    <option value="NR">Nauru</option>
                                                    <option value="NP">Nepal</option>
                                                    <option value="NL">Netherlands</option>
                                                    <option value="NC">New Caledonia</option>
                                                    <option value="NZ">New Zealand</option>
                                                    <option value="NI">Nicaragua</option>
                                                    <option value="NE">Niger</option>
                                                    <option value="NG">Nigeria</option>
                                                    <option value="NU">Niue</option>
                                                    <option value="NF">Norfolk Island</option>
                                                    <option value="MP">Northern Mariana Islands</option>
                                                    <option value="NO">Norway</option>
                                                    <option value="OM">Oman</option>
                                                    <option value="PK">Pakistan</option>
                                                    <option value="PW">Palau</option>
                                                    <option value="PS">Palestinian Territory, Occupied</option>
                                                    <option value="PA">Panama</option>
                                                    <option value="PG">Papua New Guinea</option>
                                                    <option value="PY">Paraguay</option>
                                                    <option value="PE">Peru</option>
                                                    <option value="PH">Philippines</option>
                                                    <option value="PN">Pitcairn</option>
                                                    <option value="PL">Poland</option>
                                                    <option value="PT">Portugal</option>
                                                    <option value="PR">Puerto Rico</option>
                                                    <option value="QA">Qatar</option>
                                                    <option value="RE">Réunion</option>
                                                    <option value="RO">Romania</option>
                                                    <option value="RU">Russian Federation</option>
                                                    <option value="RW">Rwanda</option>
                                                    <option value="BL">Saint Barthélemy</option>
                                                    <option value="SH">Saint Helena, Ascension and Tristan da Cunha</option>
                                                    <option value="KN">Saint Kitts and Nevis</option>
                                                    <option value="LC">Saint Lucia</option>
                                                    <option value="MF">Saint Martin (French part)</option>
                                                    <option value="PM">Saint Pierre and Miquelon</option>
                                                    <option value="VC">Saint Vincent and the Grenadines</option>
                                                    <option value="WS">Samoa</option>
                                                    <option value="SM">San Marino</option>
                                                    <option value="ST">Sao Tome and Principe</option>
                                                    <option value="SA">Saudi Arabia</option>
                                                    <option value="SN">Senegal</option>
                                                    <option value="RS">Serbia</option>
                                                    <option value="SC">Seychelles</option>
                                                    <option value="SL">Sierra Leone</option>
                                                    <option value="SG">Singapore</option>
                                                    <option value="SX">Sint Maarten (Dutch part)</option>
                                                    <option value="SK">Slovakia</option>
                                                    <option value="SI">Slovenia</option>
                                                    <option value="SB">Solomon Islands</option>
                                                    <option value="SO">Somalia</option>
                                                    <option value="ZA">South Africa</option>
                                                    <option value="GS">South Georgia and the South Sandwich Islands</option>
                                                    <option value="SS">South Sudan</option>
                                                    <option value="ES">Spain</option>
                                                    <option value="LK">Sri Lanka</option>
                                                    <option value="SD">Sudan</option>
                                                    <option value="SR">Suriname</option>
                                                    <option value="SJ">Svalbard and Jan Mayen</option>
                                                    <option value="SZ">Swaziland</option>
                                                    <option value="SE">Sweden</option>
                                                    <option value="CH">Switzerland</option>
                                                    <option value="SY">Syrian Arab Republic</option>
                                                    <option value="TW">Taiwan, Province of China</option>
                                                    <option value="TJ">Tajikistan</option>
                                                    <option value="TZ">Tanzania, United Republic of</option>
                                                    <option value="TH">Thailand</option>
                                                    <option value="TL">Timor-Leste</option>
                                                    <option value="TG">Togo</option>
                                                    <option value="TK">Tokelau</option>
                                                    <option value="TO">Tonga</option>
                                                    <option value="TT">Trinidad and Tobago</option>
                                                    <option value="TN">Tunisia</option>
                                                    <option value="TR">Turkey</option>
                                                    <option value="TM">Turkmenistan</option>
                                                    <option value="TC">Turks and Caicos Islands</option>
                                                    <option value="TV">Tuvalu</option>
                                                    <option value="UG">Uganda</option>
                                                    <option value="UA">Ukraine</option>
                                                    <option value="AE">United Arab Emirates</option>
                                                    <option value="GB">United Kingdom</option>
                                                    <option value="US">United States</option>
                                                    <option value="UM">United States Minor Outlying Islands</option>
                                                    <option value="UY">Uruguay</option>
                                                    <option value="UZ">Uzbekistan</option>
                                                    <option value="VU">Vanuatu</option>
                                                    <option value="VE">Venezuela, Bolivarian Republic of</option>
                                                    <option value="VN">Viet Nam</option>
                                                    <option value="VG">Virgin Islands, British</option>
                                                    <option value="VI">Virgin Islands, U.S.</option>
                                                    <option value="WF">Wallis and Futuna</option>
                                                    <option value="EH">Western Sahara</option>
                                                    <option value="YE">Yemen</option>
                                                    <option value="ZM">Zambia</option>
                                                    <option value="ZW">Zimbabwe</option>
                                                </select>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!--end: Form Wizard Step 4-->

                        <!--begin: Form Wizard Step 5-->
                        <div class="kt-wizard-v1__content" data-ktwizard-type="step-content">
                            <div class="kt-heading kt-heading--md">Review your Details and Submit</div>
                            <div class="kt-form__section kt-form__section--first">
                                <div class="kt-wizard-v1__review">
                                    <div class="kt-wizard-v1__review-item">
                                        <div class="kt-wizard-v1__review-title">
                                            Current Address
                                        </div>
                                        <div class="kt-wizard-v1__review-content">
                                            Address Line 1<br>
                                            Address Line 2<br>
                                            Melbourne 3000, VIC, Australia
                                        </div>
                                    </div>
                                    <div class="kt-wizard-v1__review-item">
                                        <div class="kt-wizard-v1__review-title">
                                            Delivery Details
                                        </div>
                                        <div class="kt-wizard-v1__review-content">
                                            Package: Complete Workstation (Monitor, Computer, Keyboard &amp; Mouse)<br>
                                            Weight: 25kg<br>
                                            Dimensions: 110cm (w) x 90cm (h) x 150cm (L)
                                        </div>
                                    </div>
                                    <div class="kt-wizard-v1__review-item">
                                        <div class="kt-wizard-v1__review-title">
                                            Delivery Service Type
                                        </div>
                                        <div class="kt-wizard-v1__review-content">
                                            Overnight Delivery with Regular Packaging<br>
                                            Preferred Morning (8:00AM - 11:00AM) Delivery
                                        </div>
                                    </div>
                                    <div class="kt-wizard-v1__review-item">
                                        <div class="kt-wizard-v1__review-title">
                                            Delivery Address
                                        </div>
                                        <div class="kt-wizard-v1__review-content">
                                            Address Line 1<br>
                                            Address Line 2<br>
                                            Preston 3072, VIC, Australia
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!--end: Form Wizard Step 5-->

                        <!--begin: Form Actions -->
                        <div class="kt-form__actions">
                            <div class="btn btn-secondary btn-md btn-tall btn-wide kt-font-bold kt-font-transform-u" data-ktwizard-type="action-prev">
                                Previous
                            </div>
                            <div class="btn btn-success btn-md btn-tall btn-wide kt-font-bold kt-font-transform-u" data-ktwizard-type="action-submit">
                                Submit
                            </div>
                            <div class="btn btn-brand btn-md btn-tall btn-wide kt-font-bold kt-font-transform-u" data-ktwizard-type="action-next">
                                Next Step
                            </div>
                        </div>
                        <!--end: Form Actions -->
                    </form>
                    <!--end: Form Wizard Form-->
                </div>
            </div>
            <div class="kt-widget12">
                <div class="kt-widget12__content">
                    <div class="kt-widget12__item">

                        <b-button class="next"  variant="outline-primary">Next</b-button>



                        <!-- Create Community Step 2 -->

                        <b-input-group
                                prepend="Description"
                                class="mt-3"
                                id="description"
                                description="description of the community"
                                label="Enter description"
                                label-for="description"

                        >
                            <b-form-input v-model="community_description" type="text"/>

                        </b-input-group>

                        <b-input-group
                                prepend="Roles"
                                class="mt-3"
                                id="roles"
                                label="Roles"
                                label-for="roles"

                        >
                            <b-form-input v-model="community_role" type="text" />
                            <b-input-group-append>
                                <b-button v-on:click="AddRole" variant="outline-success">Add</b-button>
                            </b-input-group-append>
                        </b-input-group>

                        <ul id="categories">
                            <li v-for="role in community_roles" :key="role">
                                <b-button v-on:click="RemoveRole(role)">{{ role }}</b-button>
                            </li>
                        </ul>

                        <b-button class="next"  variant="outline-primary">Next</b-button>




                        <!-- Create Community Step 3 -->
                        <b-row class="my-1" >
                            <b-col sm="3">
                                <label for="dataTypeName">Data Type Name :</label>
                            </b-col>
                            <b-col sm="9">
                                <b-form-input id="dataTypeName" v-model="dataTypeName" type="text"></b-form-input>
                            </b-col>
                        </b-row>
                        <b-list-group >
                            <b-list-group-item  href="#" v-for="(data,index) in community_data" :key="index" v-on:click="RemoveInput(data)"> <b-form-input v-model="community_data[index].name" placeholder="Name of the field"></b-form-input>{{data.type}}</b-list-group-item>
                        </b-list-group>
                        <>
                        <b-list-group>
                            <b-list-group-item href="#" v-on:click="AddInput('Text')">Text</b-list-group-item>
                            <b-list-group-item href="#" v-on:click="AddInput('Number')" >Number</b-list-group-item>
                            <b-list-group-item href="#" v-on:click="AddInput('Image')">Image</b-list-group-item>
                            <b-list-group-item href="#" v-on:click="AddInput('Date')">Date</b-list-group-item>
                            <b-list-group-item href="#" v-on:click="AddInput('GeoLocation')" >GeoLocation</b-list-group-item>
                            <b-list-group-item href="#" v-on:click="AddInput('Boolean')" >Boolean</b-list-group-item>
                            <b-list-group-item href="#" style='background: #eee'>- Add a Data Template -</b-list-group-item>
                            <b-list-group-item href="#" v-on:click="AddInput('RSVP')" >RSVP</b-list-group-item>
                            <b-list-group-item href="#" v-on:click="AddInput('QA')" >Question & Answer</b-list-group-item>
                        </b-list-group>
                        <b-button   variant="success">+ Add More Data Type</b-button>
                        <br></br>
                        <b-button class="next" v-on:click="CreateDataType" variant="outline-primary">Next</b-button>




                        <!-- Create Community Step 4 -->

                        <b-row class="my-1" >
                            <b-col sm="3">
                                <label for="dataTypeName">Invite People :</label>
                            </b-col>
                            <b-col sm="9">
                                <b-form-input id="dataTypeName" value="https://communal-cloud.com/12321" disabled type="text"></b-form-input>
                            </b-col>
                        </b-row>
                        <b-row>OR</b-row>
                        <b-row>
                            <b-input-group
                                    prepend="e-mail"
                                    class="mt-3"
                                    id="email"
                                    label="E-mail"
                                    label-for="email"

                            >
                                <b-form-input v-model="email" type="email" />
                                <b-input-group-append>
                                    <b-button v-on:click="AddEmail" variant="outline-success">Invite</b-button>
                                </b-input-group-append>
                            </b-input-group>
                            <ul id="categories">
                                <li v-for="email in community_emails" :key="email">
                                    <b-button v-on:click="RemoveMail(email)">{{ email }}</b-button>
                                </li>
                            </ul>
                        </b-row>

                        <b-button class="next"  variant="outline-primary">Finish</b-button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import {mapState, mapMutations} from 'vuex';

  export default {
    computed: {
   ...mapState([
     'community_roles',
     'community_data',
     'dataTypeName'
   ])
    },
    
    data() {
      return {
        name: '',
        community_name : '',
        community_purpose : '',
        community_category : '',
        community_description:'',
        community_role:'',
        
        community_categories:[],
        dataTypes:[],
        dataType:{},
        
        email:'',
        field_options: ['Required', 'Human Input', 'Saved'],
        community_emails:[]
       
      }
    },
    
    methods:{
     AddCategory(){
       this.community_categories.push(this.community_category);
     },
     RemoveCategory(){

     },
     AddRole(){
       this.community_roles.push(this.community_role);
     },
     RemoveRole(){
       
     },
     AddInput(type){
       this.community_data.push({'type' : type, name: ''});
     },
     RemoveInput(type){

     },
     CreateDataType(){
       this.dataTypes.push( {'name' : this.dataTypeName , ...this.dataType} ) 
       console.log(this.dataTypes)
     },
     AddEmail(){
       this.community_emails.push(this.email);
     },
     RemoveMail(){

     },
    
     
    }
          
}


      /* toggleModal(step) {
        // We pass the ID of the button that we want to return focus to
        // when the modal has hidden
        console.log(this.$refs)
        this.$root.$emit('bv::toggle::modal', step)
       // this.$refs[step].toggle('#'+step)
      }

*/
</script>




