with open(r'..\.git/hooks/pre-push', 'tw') as file:
    file.write(r"""#!/bin/sh
git stash -q --keep-index
source backend/venv/Scripts/activate
cd backend
./manage.py test
RESULT=$?

deactivate
cd ..

[ $RESULT -ne 0 ] && echo "
------------------
Result: FAIL TESTS
------------------
"

git stash pop -q
[ $RESULT -ne 0 ] && exit 1
exit 0
""")
