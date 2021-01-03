
class EasyDict(dict):
    def __init__(self, *args, **kwargs): super().__init__(*args, **kwargs)
    def __getattr__(self, name): return self[name]
    def __setattr__(self, name, value): self[name] = value
    def __delattr__(self, name): del self[name]

# the following is from train.py it is the signature for the commandline
# py.arg('--dataset', type=str, default='horse2zebra')
# py.arg('--datasets_dir', default='datasets')
# py.arg('--load_size', type=int, default=286)  # load image to this size
# py.arg('--crop_size', type=int, default=256)  # then crop to this size
# py.arg('--batch_size', type=int, default=1)
# py.arg('--epochs', type=int, default=200)
# py.arg('--epoch_decay', type=int, default=100)  # epoch to start decaying learning rate
# py.arg('--lr', type=float, default=0.0002)
# py.arg('--beta_1', type=float, default=0.5)
# py.arg('--adversarial_loss_mode', default='lsgan', choices=['gan', 'hinge_v1', 'hinge_v2', 'lsgan', 'wgan'])
# py.arg('--gradient_penalty_mode', default='none', choices=['none', 'dragan', 'wgan-gp'])
# py.arg('--gradient_penalty_weight', type=float, default=10.0)
# py.arg('--cycle_loss_weight', type=float, default=10.0)
# py.arg('--identity_loss_weight', type=float, default=0.0)
# py.arg('--pool_size', type=int, default=50)  # pool size to store fake samples

# must have all these attributes

args = EasyDict()

args.dataset = 'horse2zebra'
args.datasets_dir = 'datasets'
args.load_size = 286
args.crop_size = 256
args.batch_size = 1
args.epochs = 200
args.epoch_decay = 100
args.lr = 0.0002
args.beta_1 = 0.5
args.adversarial_loss_mode = 'lsgan'
args.gradient_penalty_mode = 'none'
args.gradient_penalty_weight = 10.0
args.cycle_loss_weight = 10.0
args.identity_loss_weight = 0.0
args.pool_size = 50

args.new_run = False
args.run_id = False
args.checkpoint_path = None

# now, if you `import config ...`
# and set `args.xyz = 123`,
# other things that `import config as args`
# will see `args.xyz == 123`