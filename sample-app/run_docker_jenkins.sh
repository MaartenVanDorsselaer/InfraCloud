# DEVASC COURSE
docker run --rm -u root -p 8080:8080 -v jenkins-data:/var/run/jenkins_home \
-v $(which docker) :/usr/bin/docker -v /var/run/docker.sock:/var/run/docker.sock \
-v "$HOME":/home --name jenkins_server jenkins/jenkins:lts
# docker run --rm --privileged -p 8080:8080 -p 50000:50000 -v jenkins-data:/var/jenkins