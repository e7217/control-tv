docker run -dit \
    --device /dev/fuse \
    --cap-add SYS_ADMIN \
    --security-opt "apparmor=unconfined" \
    --env "WEBDRIVE_USERNAME=<YourUserName>" \
    --env "WEBDRIVE_PASSWORD=<SuperSecretPassword>" \
    --env "WEBDRIVE_URL=https://dav.box.com/dav" \
    --env "DAVFS2_ASK_AUTH=0" \
    -v /mnt/tmp:/mnt/webdrive:rshared \
    efrecon/webdav-client