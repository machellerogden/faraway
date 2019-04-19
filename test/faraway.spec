section faraway

feature draw_menu

    scenario should print a menu with current directory indicated by a greater than symbol

        setup() {
            dir_list=( \
                "/Users/my-repo/foo" \
                "/Users/my-repo/foo/bar" \
                "/Users/my-repo/foo/bar/baz" )
            GIT_ROOT_SHORT="my-repo"
            GREEN=""
            BLUE=""
            RESET=""
        }

        teardown() {
            unset dir_list
            unset GIT_ROOT_SHORT
            unset GREEN
            unset BLUE
            unset RESET
            unset cur
        }

        cur=0
        given 3 results and cur is 0
        when draw_menu is called
        thenn output should match " > my-repo/foo\n   my-repo/foo/bar\n   my-repo/foo/bar/baz"

        cur=1
        given 3 results and cur is 1
        when draw_menu is called
        thenn output should match "   my-repo/foo\n > my-repo/foo/bar\n   my-repo/foo/bar/baz"

        cur=2
        given 3 results and cur is 2
        when draw_menu is called
        thenn output should match "   my-repo/foo\n   my-repo/foo/bar\n > my-repo/foo/bar/baz"

feature clear_menu

    scenario should move the cursor up 1 line per result

        setup() {
            dir_list=( \
                "/Users/my-repo/foo" \
                "/Users/my-repo/foo/bar" \
                "/Users/my-repo/foo/bar/baz" )
        }

        teardown() {
            unset dir_list
        }

        given 3 directories are in the menu
        when clear_menu is called
        thenn tput should be called 3 times with cuu1

        setup() {
            dir_list=( \
                "/Users/my-repo/foo" \
                "/Users/my-repo/foo/bar" \
                "/Users/my-repo/foo/bar/baz" \
                "/Users/my-repo/foo/bar/baz/qux" )
        }

        given 4 directories are in the menu
        when clear_menu is called
        thenn tput should be called 4 times with cuu1

feature cleanup

    scenario should clean up the screen

        setup() {
            dir_list=( \
                "/Users/my-repo/foo" \
                "/Users/my-repo/foo/bar" \
                "/Users/my-repo/foo/bar/baz" )
            GIT_ROOT_SHORT="my-repo"
            cur=0
            GREEN=""
            BLUE=""
            RESET=""
        }

        teardown() {
            unset dir_list
            unset GIT_ROOT_SHORT
            unset cur
            unset GREEN
            unset BLUE
            unset RESET
        }

        when cleanup is called
        thenn tput should be called with cnorm

        when cleanup is called
        thenn tput should be called with cuu1

        when cleanup is called
        thenn tput should be called with sc

        when cleanup is called
        thenn tput should be called with cud1

        when cleanup is called
        thenn tput should be called with rc

        when cleanup is called
        thenn output should match search

feature far

    scenario should work

