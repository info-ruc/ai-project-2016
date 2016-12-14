set -x


NET=resnet-20
EXTRA_ARGS=${array[@]:3:$len}
EXTRA_ARGS_SLUG=${EXTRA_ARGS// /_}

solver=proto/solver.prototxt
LOG="log/${NET}_${EXTRA_ARGS_SLUG}_`date +'%Y-%m-%d_%H-%M-%S'`.log"
exec &> >(tee -a "$LOG")
echo Logging output to "$LOG"

caffe train  \
    -solver ${solver} \
    -sighup_effect stop \
    ${EXTRA_ARGS}

set +x
