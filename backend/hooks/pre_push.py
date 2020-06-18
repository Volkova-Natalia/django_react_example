with open(r'..\.git/hooks/pre-push', 'tw') as file:
    file.write(r"""#!/bin/sh
git stash -q --keep-index
source backend/venv/Scripts/activate
cd backend
./manage.py test
RESULT=$?

[ $RESULT -ne 0 ] && echo "
------------------
Result: FAIL TESTS
------------------
"

deactivate
cd ..

git stash pop -q
[ $RESULT -ne 0 ] && exit 1
exit 0
""")
