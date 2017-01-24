import requests, os
import frontmatter, git, json

# https://gitpython.readthedocs.io/en/stable/tutorial.html#the-commit-object

# Set the request parameters
url = 'https://kbplanning.zendesk.com/api/v2/help_center/en-us/articles.json'
user = os.environ['KB_USER']
pwd = os.environ['KB_PASSWORD']

# @TODO exclude README.md files

def get_article(article_id):
    """
      Args:
      param1 (int): The first parameter.
      param2 (str): The second parameter.

    Returns:
      bool: The return value. True for success, False otherwise.
    """
    # Check if the article ID exists
    print 'Load an Article -> get_article()'

    # https://developer.zendesk.com/rest_api/docs/help_center/articles#show-article
    article_url = 'help_center/en-us/articles/%d.json' % (article_id)
    hc_article = zd_request(article_url)

    # Check if article_id exists in the Help Center
    if 'id' in hc_article['article'].keys():
        print 'Success - An article exists with ID - %d -> get_article()' % (hc_article['article']['id'])
        return hc_article
    else:
        print 'Error - Unable find an article with ID - %d' % (article_id)
        return

def create_article(article):
    """
    Args:
      article (article): An instance of a Help Center Article

    Returns:
      article: An instance of a new Help Center Article.
    """
    create_url = '/api/v2/help_center/en-us/articles.json'

    # Create a new article
    new_article = zd_request(create_url)
    # Check if article_id exists in .md
    if new_article:
        print 'Success - An article was created in the helpcenter ID - XXXX'
        # @TODO - update_git_article
        update_git_article(article)
    else:
        print 'Error - Unable to create a new article in the helpcenter'
    
    return new_article


def update_article(article):
    """
    Args:
      article (article): An instance of a Help Center Article

    Returns:
      article: An instance of the updated Help Center Article.
    """
    print 'Check if article_id exists in the Help Center -> update_article()'
    # Check if the article exists in the helpcenter
    hc_article = get_article(article['id'])
    # if the article exists in the helpcenter then update

    if hc_article:
        print 'Success - An article exists with ID - %d -> update_article()' % article['id']

        # https://developer.zendesk.com/rest_api/docs/help_center/articles#update-article
        """curl https://kbplanning.zendesk.com/api/v2/help_center/articles/115001647907/translations/en-us.json \
        -d '{"translation": {"body": "if the article exists in the helpcenter then update"}}'
          -v -u {email_address}:{password} -X PUT -H "Content-Type: application/json"
        """
        update_url = 'help_center/articles/%d/translations/en-us' %  article['id']
        data = {'translation':{'body': article.content }}
        updated_article = zd_request(update_url, data, 'PUT')

        if updated_article:
            print 'Success - An article was updated with ID - %d' % updated_article['translation']['id']
        else:
            print 'Error - Unable to update article'

    # @TODO should we create one anyway? Discuss?
    print "Return an instance of the updated_article -> update_article()"
    return updated_article

def update_git_article():
    """

    Returns:
      bool: The return value. True for success, False otherwise.
    """
    # Check if ZD_ID exists
    # if not, append it to the front matter
    # if so set it to the new ZD_ID from create_article
    # Create a new commit on the PR branch
    # Merge the new commit to master \
    # (This could happen as part of the GH merge && check for conflicts?)
    return

def git_diff(branch1, branch2):
    """
      Args:
      param1 (int): The first parameter.
      param2 (str): The second parameter.

    Returns:
      bool: The return value. True for success, False otherwise.
    """
    log_format = '--name-only'
    commits = []
    git_repo = git.Git('/path/to/git/repo')
    differ = git_repo.diff('%s..%s' % (branch1, branch2), log_format).split("\n")
    for line in differ:
        if len(line):
            commits.append(line)

    #for commit in commits:
    #    print '*%s' % (commit)
    return commits

def zd_request(u, req_data=None, method='GET', ): 
    """
      Args:
      method (str): The first parameter.
      data (str): The second parameter.

    Returns:
      bool: The return value. True for success, False otherwise.
    """

    # Package the data in a dictionary matching the expected JSON
    #req_data = {'article': {'title': 'if the article exists in the helpcenter then update'}}
    print req_data
    #content = {'ticket': {'comment': {'body':data}}}

    # Encode the data to create a JSON payload
    payload = json.dumps(req_data)
    headers = {'Content-type': 'application/json'}

    # URL
    print 'Perform an HTTP Request to Zendesk -> zd_request()'
    req_url = 'https://kbplanning.zendesk.com/api/v2/%s' % u
    print req_url

    if method is 'POST':
        print "You trying to POST bro?"
        response = requests.post(req_url, data=payload, auth=(user, pwd), headers=headers)
    elif method is 'PUT':
        print "You trying to PUT bro?"
        print payload
        response = requests.put(req_url, data=payload, auth=(user, pwd), headers=headers)
    else:
        print "You trying to GET bro?"
        response = requests.get(req_url, auth=(user, pwd))

    # Do the HTTP get request
    #response = requests.get(req_url, auth=(user, pwd))
    # Check for HTTP codes other than 200
    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting.')

    # Decode the JSON response into a dictionary and use the data
    data = response.json()

    # print data
    return data

def load_article_from_source():
    """
      Args:
      param2 (str): The second parameter.

    Returns:
      bool: The return value. True for success, False otherwise.
    """
    # TODO loop through diff for .md files (Exclude README.md)
    # Load the markdown from the article
    article = frontmatter.load('tests/article_with_id.md')
    #article = frontmatter.load('tests/article_without_id.md')

    # Extract the Article id
    if 'id' in article.keys():
        print 'I HAVE AND ID -> load_article_from_source()'
        update_article(article)
    else:
        print 'NO ID FOR YOU -> load_article_from_source()'
        return
        create_article(article)

def main():
    """  
    """
  # https://gitpython.readthedocs.io/en/stable/tutorial.html#the-commit-object
  # get_article(1150016479071)
    load_article_from_source()
    
if __name__ == "__main__":
    main()
