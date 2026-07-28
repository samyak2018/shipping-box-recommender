(venv) PS C:\Sanskruti\internproject\box-recommender> python manage.py test
Found 15 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
...............
----------------------------------------------------------------------
Ran 15 tests in 0.161s

OK
Destroying test database for alias 'default'...
(venv) PS C:\Sanskruti\internproject\box-recommender> python manage.py test -v 2
Found 15 test(s).
Creating test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...
Operations to perform:
  Synchronize unmigrated apps: messages, staticfiles
  Apply all migrations: admin, auth, contenttypes, orders, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying orders.0001_initial... OK
  Applying sessions.0001_initial... OK
System check identified no issues (0 silenced).
test_box_invalid_when_order_is_too_heavy (orders.tests.BoxRecommenderTests.test_box_invalid_when_order_is_too_heavy) ... ok
test_box_invalid_when_total_volume_is_too_large (orders.tests.BoxRecommenderTests.test_box_invalid_when_total_volume_is_too_large) ... ok
test_calculate_box_volume (orders.tests.BoxRecommenderTests.test_calculate_box_volume) ... ok
test_calculate_order_volume (orders.tests.BoxRecommenderTests.test_calculate_order_volume) ... ok
test_calculate_order_weight (orders.tests.BoxRecommenderTests.test_calculate_order_weight) ... ok
test_calculate_product_volume (orders.tests.BoxRecommenderTests.test_calculate_product_volume) ... ok
test_cheaper_valid_box_is_preferred_over_smaller_box (orders.tests.BoxRecommenderTests.test_cheaper_valid_box_is_preferred_over_smaller_box) ... ok
test_get_valid_boxes (orders.tests.BoxRecommenderTests.test_get_valid_boxes) ... ok
test_inactive_box_is_ignored (orders.tests.BoxRecommenderTests.test_inactive_box_is_ignored) ... ok
test_product_does_not_fit_when_too_large (orders.tests.BoxRecommenderTests.test_product_does_not_fit_when_too_large) ... ok
test_product_fits_box (orders.tests.BoxRecommenderTests.test_product_fits_box) ... ok
test_product_fits_box_after_rotation (orders.tests.BoxRecommenderTests.test_product_fits_box_after_rotation) ... ok
test_recommend_box_returns_none_when_no_box_fits (orders.tests.BoxRecommenderTests.test_recommend_box_returns_none_when_no_box_fits) ... ok
test_recommend_cheapest_valid_box (orders.tests.BoxRecommenderTests.test_recommend_cheapest_valid_box) ... ok
test_smaller_box_selected_when_cost_is_equal (orders.tests.BoxRecommenderTests.test_smaller_box_selected_when_cost_is_equal) ... ok

----------------------------------------------------------------------
Ran 15 tests in 0.169s


















(venv) PS C:\Sanskruti\internproject\box-recommender> python manage.py test --verbosity=2
Found 31 test(s).
Creating test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...
Operations to perform:
  Synchronize unmigrated apps: messages, staticfiles
  Apply all migrations: admin, auth, contenttypes, orders, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying orders.0001_initial... OK
  Applying sessions.0001_initial... OK
System check identified no issues (0 silenced).
test_box_invalid_when_order_is_too_heavy (orders.tests.BoxRecommenderTests.test_box_invalid_when_order_is_too_heavy) ... ok
test_box_invalid_when_total_volume_is_too_large (orders.tests.BoxRecommenderTests.test_box_invalid_when_total_volume_is_too_large) ... ok
test_calculate_box_volume (orders.tests.BoxRecommenderTests.test_calculate_box_volume) ... ok
test_calculate_order_volume (orders.tests.BoxRecommenderTests.test_calculate_order_volume) ... ok
test_calculate_order_weight (orders.tests.BoxRecommenderTests.test_calculate_order_weight) ... ok
test_calculate_product_volume (orders.tests.BoxRecommenderTests.test_calculate_product_volume) ... ok
test_cheaper_valid_box_is_preferred_over_smaller_box (orders.tests.BoxRecommenderTests.test_cheaper_valid_box_is_preferred_over_smaller_box) ... ok
test_get_valid_boxes (orders.tests.BoxRecommenderTests.test_get_valid_boxes) ... ok
test_inactive_box_is_ignored (orders.tests.BoxRecommenderTests.test_inactive_box_is_ignored) ... ok
test_product_does_not_fit_when_too_large (orders.tests.BoxRecommenderTests.test_product_does_not_fit_when_too_large) ... ok
test_product_fits_box (orders.tests.BoxRecommenderTests.test_product_fits_box) ... ok
test_product_fits_box_after_rotation (orders.tests.BoxRecommenderTests.test_product_fits_box_after_rotation) ... ok
test_recommend_box_returns_none_when_no_box_fits (orders.tests.BoxRecommenderTests.test_recommend_box_returns_none_when_no_box_fits) ... ok
test_recommend_cheapest_valid_box (orders.tests.BoxRecommenderTests.test_recommend_cheapest_valid_box) ... ok
test_smaller_box_selected_when_cost_is_equal (orders.tests.BoxRecommenderTests.test_smaller_box_selected_when_cost_is_equal) ... ok
test_create_order_page_loads_successfully (orders.tests.OrderFormAndViewTests.test_create_order_page_loads_successfully) ... ok
test_create_order_page_uses_correct_template (orders.tests.OrderFormAndViewTests.test_create_order_page_uses_correct_template) ... ok
test_empty_order_submission_does_not_create_order (orders.tests.OrderFormAndViewTests.test_empty_order_submission_does_not_create_order) ... ok
test_nonexistent_order_returns_404 (orders.tests.OrderFormAndViewTests.test_nonexistent_order_returns_404) ... ok
test_order_detail_displays_message_when_no_box_fits (orders.tests.OrderFormAndViewTests.test_order_detail_displays_message_when_no_box_fits) ... ok
test_order_detail_displays_order_items (orders.tests.OrderFormAndViewTests.test_order_detail_displays_order_items) ... ok
test_order_detail_displays_recommended_box (orders.tests.OrderFormAndViewTests.test_order_detail_displays_recommended_box) ... ok
test_order_detail_page_loads_successfully (orders.tests.OrderFormAndViewTests.test_order_detail_page_loads_successfully) ... ok
test_order_form_accepts_valid_quantities (orders.tests.OrderFormAndViewTests.test_order_form_accepts_valid_quantities) ... ok
test_order_form_contains_product_fields (orders.tests.OrderFormAndViewTests.test_order_form_contains_product_fields) ... ok
test_order_form_rejects_empty_order (orders.tests.OrderFormAndViewTests.test_order_form_rejects_empty_order) ... ok
test_order_form_rejects_negative_quantity (orders.tests.OrderFormAndViewTests.test_order_form_rejects_negative_quantity) ... ok
test_valid_submission_creates_correct_order_items (orders.tests.OrderFormAndViewTests.test_valid_submission_creates_correct_order_items) ... ok
test_valid_submission_creates_order (orders.tests.OrderFormAndViewTests.test_valid_submission_creates_order) ... ok
test_valid_submission_redirects_to_order_detail (orders.tests.OrderFormAndViewTests.test_valid_submission_redirects_to_order_detail) ... ok
test_zero_quantity_product_does_not_create_order_item (orders.tests.OrderFormAndViewTests.test_zero_quantity_product_does_not_create_order_item) ... ok

----------------------------------------------------------------------
Ran 31 tests in 0.287s

OK
Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...