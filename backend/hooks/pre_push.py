with open(r'..\.git/hooks/pre-push', 'tw') as file:
    file.write(r"""#!/bin/sh
git stash -q --keep-index
source venv/Scripts/activate
./manage.py test
RESULT=$?

[ $RESULT -ne 0 ] && echo "
------------------
Result: FAIL TESTS
------------------
"

deactivate

git stash pop -q
[ $RESULT -ne 0 ] && exit 1
exit 0
""")
