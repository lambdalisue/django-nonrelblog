#!/bin/bash
#
# Script for Downloading and linking required packages 
# to run Django-nonrel based app
#

# Absolute path of oneself
ROOT=$(cd $(dirname $0);pwd)

# Define
PACKAGE_DIR=$ROOT/../.packages
SOURCE_DIR=$ROOT/../src/nonrelblog

# --- commands

function download()
{
    hg clone http://bitbucket.org/wkornewald/django-nonrel $PACKAGE_DIR/django-nonrel
    hg clone http://bitbucket.org/wkornewald/djangotoolbox $PACKAGE_DIR/djangotoolbox
    hg clone http://bitbucket.org/wkornewald/django-dbindexer $PACKAGE_DIR/django-dbindexer
    hg clone http://bitbucket.org/twanschik/django-autoload $PACKAGE_DIR/django-autoload
    hg clone http://bitbucket.org/lambdalisue/djangoappengine $PACKAGE_DIR/djangoappengine
    return 0
}

function link()
{
    ln -sf $PACKAGE_DIR/django-nonrel/django $SOURCE_DIR/django
    ln -sf $PACKAGE_DIR/djangoappengine $SOURCE_DIR/djangoappengine
    ln -sf $PACKAGE_DIR/djangotoolbox/djangotoolbox $SOURCE_DIR/djangotoolbox
    ln -sf $PACKAGE_DIR/django-dbindexer/dbindexer $SOURCE_DIR/dbindexer
    ln -sf $PACKAGE_DIR/django-autoload/autoload $SOURCE_DIR/autoload
    return 0
}

function install()
{
    download
    link
    return 0
}
function update()
{
    cd $PACKAGE_DIR/django-nonrel
    hg update
    cd $PACKAGE_DIR/django-dbindexer
    hg update
    cd $PACKAGE_DIR/django-autoload
    hg update
    cd $PACKAGE_DIR/djangotoolbox
    hg update
    cd $PACKAGE_DIR/djangoappengine
    hg update
    return 0
}
function clean()
{
    rm -rf $PACKAGE_DIR/django-nonrel
    rm -rf $PACKAGE_DIR/djangoappengine
    rm -rf $PACKAGE_DIR/djangotoolbox
    rm -rf $PACKAGE_DIR/django-dbindexer
    rm -rf $PACKAGE_DIR/django-autoload
    rm -rf $SOURCE_DIR/django
    rm -rf $SOURCE_DIR/djangoappengine
    rm -rf $SOURCE_DIR/djangotoolbox
    rm -rf $SOURCE_DIR/djangotoolbox
    rm -rf $SOURCE_DIR/autoload
    return 0
}

# --- main block
# attempt to invoke the first param as the command
# and subsequent param as parameters for that command
# Note: Bash can only go up to $9 so we use ${10}..${12}, and so on
$1 "$2" "$3" "$4" "$5" "$6" "$7" "$8" "$9" "${10}" "${11}" "${12}"
result=$?
if (( $result == 127 )); then
   echo "ERROR: command $1 is not implemented"
   exit 127
fi
exit $result
