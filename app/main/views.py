from flask import render_template,abort,request,redirect,url_for,jsonify
from . import main
from .. import photos, client
import boto3





@main.route('/', methods = ['POST', 'GET'])
def update_pic():
    if request.method == 'POST':
        if 'photo' in request.files:
            filename = photos.save(request.files['photo'])
            path = f'app/static/photos/{filename}'
            #Uploading a file to space
            client.upload_file(path, 'test-deliverly', filename)
            return render_template('success.html')

    return render_template('upload.html')

@main.route('/download/<filename>', methods = ['GET'])
def download(filename):
    #downloading a file from space
    client.download_file('test-deliverly',
                     filename,
                     'd.png')
    return jsonify({"message":"file downloaded successfully!"})      

@main.route('/list-all', methods = ['GET'])
def listing_files():
    #listing all files in a space
    response = client.list_objects(Bucket='test-deliverly')
    results = []
        #print(obj['Key'])  
    for obj in response['Contents']:
        file_obj = {}
        file_obj['name']=obj['Key']
        results.append(file_obj)

    return jsonify({"files":results})            