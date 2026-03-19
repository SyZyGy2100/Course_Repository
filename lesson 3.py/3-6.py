is_logged_in = True
is_admin = False

if is_logged_in:
    print("user is logged in.")
    if is_admin:
        print("show admin dashboard.")
    else:
        print("show regular user dashboard.")
else:
    print("redirect to login page.")        