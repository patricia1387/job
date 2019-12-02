# job
Repository with example of Job and BuilConfig for this job, short manual how to work with it s here:

1. You need to have installed minishift, or access to openshift
2. You need to login via web console and via command line, via command line you login with command:
  oc login
3. You need to create project via wen console or command line, via command line you do it with this command:
  oc new-project "project-name"
4. You need to create imagestream:
  oc create imagestream "imagestream name"
5. You need to upload BuildConfig you can do it via webconsole "Import yaml/json"
6. Wait until build of BuildConfig end
7. Create job:
  oc create -f "job name.yaml"



