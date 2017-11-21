from selenium.webdriver.common.by import By


class Locators(object):
    register_id_homepage = (By.ID,'loginPageRegister1')
    register_id_homepage_locator = 'loginPageRegister1'
    mpower_logo = (By.XPATH, "//img[@alt='mPower Logo']")
    mpower_logo_locator = "//img[@alt='mPower Logo']"
    mpower_logo_locator_css = 'img.logo'
    firstName_id = (By.ID, 'firstName')
    firstName_locator = 'firstName'
    test_firstName = 'Jack'
    lastName_id = (By.ID, 'lastName')
    lastName_locator = 'lastName'
    test_LastName = 'Reacher'
    educatorRole_id = (By.ID, 'educatorRoleId')
    educatorRole_locator = 'educatorRoleId'
    test_educatorRole = 'Coach'
    board_id_locator = 'boardId'
    board_id =(By.ID,'boardId')
    test_board_name = 'Toronto DSB'
    school_id = (By.ID, 'schoolId')
    school_locator =  'schoolId'
    test_school_name = 'Adam Beck'
    email_id = (By.ID, 'email')
    email_locator = 'email'
    test_valid_email_name = 'jackrear@tdsb.on.ca'
    test_invalid_email_name = 'jackrear@toronto.com'
    userEmailConfirm_id = (By.ID, 'userEmailConfirm')
    userEmailConfirm_locator = 'userEmailConfirm'
    userPassword_id = (By.ID, 'userPassword')
    userPassword_locator = 'userPassword'
    test_valid_password = "Jack@123"
    userPasswordConfirm_id = (By.ID, 'userPasswordConfirm')
    userPasswordConfirm_locator = 'userPasswordConfirm'
    source_id = (By.ID, 'source')
    source_locator = 'source'
    test_source_name = 'Conference'
    source_other_id = (By.ID, 'sourceOther')
    source_other_locator = 'sourceOther'
    agreement_id = (By.ID, 'agreement')
    agreement_locator = 'agreement'
    emailPromos_id = (By.ID, 'emailPromos')
    emailPromos_locator = 'emailPromos'
    registerSubmit_id = (By.ID, 'registerSubmit')
    registerSubmit_locator = 'registerSubmit'
    registerCancel_css = (By.CSS_SELECTOR,'button.btn.btn-cancel')
    registerCancel_locator = 'button.btn.btn-cancel'
    invalid_email_error_message = 'The email you want to use does not match the email of your school board. The domain of your email address should be tdsb.on.ca'
    firstname_error_message = 'Please enter your first name'
    lastname_error_message = 'Please enter your last name'
    role_error_message = 'Please select a role'
    board_error_message = 'Please select a school board'
    school_error_message = 'Please add your school'
    email_error_message = 'Please enter a valid email address'
    password_error_message = 'Your password must be 8-32 characters long'
    source_error_message = 'Please tell us where you heard about mPower'
    agreement_error_message = 'You must check agree to continue'
    email_mismatch_error = 'Please make sure your email matches'
    password_mismatch_error = 'Your passwords do not match'
    add_new_school_locator = "//a[contains(text(),'click here')]"
    new_school_text_locator = 'tempSchoolName'
    test_new_school_name = 'My Public School'
    test_invalid_name = 'testtesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttest'
    invalid_first_name_error_message = 'The first name specified is of an invalid length'
    invalid_last_name_error_message = 'The last name specified is of an invalid length'
    invalid_first_name_spl_char_error_message = 'The first name may only contain alphanumeric characters and single spaces.'
    invalid_last_name_spl_char_error_message = 'The last name may only contain alphanumeric characters and single spaces.'
    test_email_id = 'test1@tdsb.on.ca'
    privacy_policy_locator = "//a[contains(text(),'Privacy Policy')]"
    user_terms_link = 'Terms of use'
    copyright_link = 'Copyright'
    back_link = 'Back'
    user_terms_message = 'Jurisdiction and Governing Law '
    privacy_policy_message = 'Personally identifiable information may include'
    copyright_message = 'Copyright and Ownership of Web Site Materials'