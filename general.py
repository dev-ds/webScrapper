import os

def create_project_dir(projectDir):
    if not os.path.exists(projectDir):
        print('creating Project : ', projectDir)
        os.makedirs(projectDir)

def create_files(projectName, baseURL):
    queue = projectName + '/queue.txt'
    crawled = projectName + '/crawled.txt'

    if not os.path.isfile(queue):
        write_file(queue, baseURL)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

# write data to the queue or crawl files for first time
def write_file(file, data):
    f = open(file, 'w')
    f.write(data)
    f.close()

#appending data to the files
def append_file(file, data):
    with open(file, 'a') as f:
        f.write(data + '\n')

# write mp3 links
def append_mp3(file, data):
    with open(file, 'a') as f:
        f.write(data + '\n')


# delete the contents of the files
def delete_file_content(file):
    with open(file, 'w') as f:
        pass

#creating sets so that its easier to handle
def file_to_set(file):
    toset = set()
    with open(file, 'r') as f:
        for line in f:
            toset.add(line.replace('\n',''))
    return toset

# write the sets back to files
def set_to_file(links, file):
    delete_file_content(file)
    for link in sorted(links):
        append_file(file, link)

def mp3_to_file(mp3Links, file):
    for key, value in mp3Links.items():
        append_mp3(file, str(key + ' - ' + value))
