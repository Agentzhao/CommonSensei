# pip install flask if not installed
# don't name your file as flask.py !

from bs4 import BeautifulSoup as bs
import requests

# create a Flask object


# function to access website to get the answer given the quesiton
def response(question):    
    question = "_".join(question.split())
    url = 'http://www.answers.com/Q/' + question
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    ans = soup.find('div', {'class' : 'answer_text'}).text.strip().replace('\n', " ")
    return ans

# load the question webpage
@app.route('/')
def load_webpage():
    return render_template('qna.html')  

# get the answer

def question():    
    if request.method == 'POST':

      reply = response(question)
      return redirect(url_for('ans',  answer = reply))

# display the answer 
@app.route('/ans/<answer>')
def ans(answer):
    return ('Answer : %s' % answer)

# run the app
if __name__ == '__main__':


