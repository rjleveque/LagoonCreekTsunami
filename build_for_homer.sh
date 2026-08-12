
export BASE_URL=/ptha/CopesHubTsunamis/LagoonCreek; jupyter book build --html --execute

echo Next:
echo '   rsync -avz _build/html/ \
    ptha@homer.u.washington.edu:public_html/CopesHubTsunamis/LagoonCreek/'
