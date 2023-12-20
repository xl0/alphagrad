# Autogenerated by nbdev

d = { 'settings': { 'branch': 'master',
                'doc_baseurl': '/tidygrad',
                'doc_host': 'https://xl0.github.io',
                'git_url': 'https://github.com/xl0/tidygrad',
                'lib_path': 'tidygrad'},
  'syms': { 'tidygrad.func': { 'tidygrad.func.BCE_loss': ('func.html#bce_loss', 'tidygrad/func.py'),
                               'tidygrad.func.CrossEntropy_loss': ('func.html#crossentropy_loss', 'tidygrad/func.py'),
                               'tidygrad.func.add': ('func.html#add', 'tidygrad/func.py'),
                               'tidygrad.func.broadcast': ('func.html#broadcast', 'tidygrad/func.py'),
                               'tidygrad.func.concat': ('func.html#concat', 'tidygrad/func.py'),
                               'tidygrad.func.div': ('func.html#div', 'tidygrad/func.py'),
                               'tidygrad.func.dropout': ('func.html#dropout', 'tidygrad/func.py'),
                               'tidygrad.func.embedding': ('func.html#embedding', 'tidygrad/func.py'),
                               'tidygrad.func.exp': ('func.html#exp', 'tidygrad/func.py'),
                               'tidygrad.func.gelu': ('func.html#gelu', 'tidygrad/func.py'),
                               'tidygrad.func.layer_norm': ('func.html#layer_norm', 'tidygrad/func.py'),
                               'tidygrad.func.log': ('func.html#log', 'tidygrad/func.py'),
                               'tidygrad.func.logexp': ('func.html#logexp', 'tidygrad/func.py'),
                               'tidygrad.func.matmul': ('func.html#matmul', 'tidygrad/func.py'),
                               'tidygrad.func.mul': ('func.html#mul', 'tidygrad/func.py'),
                               'tidygrad.func.neg': ('func.html#neg', 'tidygrad/func.py'),
                               'tidygrad.func.pow': ('func.html#pow', 'tidygrad/func.py'),
                               'tidygrad.func.relu': ('func.html#relu', 'tidygrad/func.py'),
                               'tidygrad.func.sigmoid': ('func.html#sigmoid', 'tidygrad/func.py'),
                               'tidygrad.func.sigmoid_gelu': ('func.html#sigmoid_gelu', 'tidygrad/func.py'),
                               'tidygrad.func.slice': ('func.html#slice', 'tidygrad/func.py'),
                               'tidygrad.func.softmax': ('func.html#softmax', 'tidygrad/func.py'),
                               'tidygrad.func.stack': ('func.html#stack', 'tidygrad/func.py'),
                               'tidygrad.func.sub': ('func.html#sub', 'tidygrad/func.py'),
                               'tidygrad.func.sum': ('func.html#sum', 'tidygrad/func.py'),
                               'tidygrad.func.tanh': ('func.html#tanh', 'tidygrad/func.py'),
                               'tidygrad.func.transpose': ('func.html#transpose', 'tidygrad/func.py')},
            'tidygrad.model': { 'tidygrad.model.Model': ('model.html#model', 'tidygrad/model.py'),
                                'tidygrad.model.Model.__init__': ('model.html#model.__init__', 'tidygrad/model.py'),
                                'tidygrad.model.Model.__repr__': ('model.html#model.__repr__', 'tidygrad/model.py'),
                                'tidygrad.model.Model.parameter_list': ('model.html#model.parameter_list', 'tidygrad/model.py'),
                                'tidygrad.model.Model.requires_grad': ('model.html#model.requires_grad', 'tidygrad/model.py'),
                                'tidygrad.model.Model.save': ('model.html#model.save', 'tidygrad/model.py')},
            'tidygrad.ops.activation': { 'tidygrad.ops.activation.Relu': ('ops.activation.html#relu', 'tidygrad/ops/activation.py'),
                                         'tidygrad.ops.activation.Relu.__init__': ( 'ops.activation.html#relu.__init__',
                                                                                    'tidygrad/ops/activation.py'),
                                         'tidygrad.ops.activation.Relu.backward': ( 'ops.activation.html#relu.backward',
                                                                                    'tidygrad/ops/activation.py'),
                                         'tidygrad.ops.activation.Sigmoid': ('ops.activation.html#sigmoid', 'tidygrad/ops/activation.py'),
                                         'tidygrad.ops.activation.Sigmoid.__init__': ( 'ops.activation.html#sigmoid.__init__',
                                                                                       'tidygrad/ops/activation.py'),
                                         'tidygrad.ops.activation.Sigmoid.backward': ( 'ops.activation.html#sigmoid.backward',
                                                                                       'tidygrad/ops/activation.py')},
            'tidygrad.ops.common': { 'tidygrad.ops.common.Add': ('ops.common.html#add', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Add.__init__': ('ops.common.html#add.__init__', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Add.backward': ('ops.common.html#add.backward', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.BaseOp': ('ops.common.html#baseop', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.BaseOp.__init__': ('ops.common.html#baseop.__init__', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.BaseOp.__repr__': ('ops.common.html#baseop.__repr__', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.BaseOp.check_backward': ( 'ops.common.html#baseop.check_backward',
                                                                                    'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.BaseOp.set_out': ('ops.common.html#baseop.set_out', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.BinaryElementwiseOp': ( 'ops.common.html#binaryelementwiseop',
                                                                                  'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.BinaryElementwiseOp.__init__': ( 'ops.common.html#binaryelementwiseop.__init__',
                                                                                           'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Broadcast': ('ops.common.html#broadcast', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Broadcast.__init__': ( 'ops.common.html#broadcast.__init__',
                                                                                 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Broadcast.backward': ( 'ops.common.html#broadcast.backward',
                                                                                 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Div': ('ops.common.html#div', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Div.__init__': ('ops.common.html#div.__init__', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Div.backward': ('ops.common.html#div.backward', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Dropout': ('ops.common.html#dropout', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Dropout.__init__': ('ops.common.html#dropout.__init__', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Dropout.backward': ('ops.common.html#dropout.backward', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Embedding': ('ops.common.html#embedding', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Embedding.__init__': ( 'ops.common.html#embedding.__init__',
                                                                                 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Embedding.backward': ( 'ops.common.html#embedding.backward',
                                                                                 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Exp': ('ops.common.html#exp', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Exp.__init__': ('ops.common.html#exp.__init__', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Exp.backward': ('ops.common.html#exp.backward', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.ExpLog': ('ops.common.html#explog', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.ExpLog.__init__': ('ops.common.html#explog.__init__', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.ExpLog.backward': ('ops.common.html#explog.backward', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Load': ('ops.common.html#load', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Load.__init__': ('ops.common.html#load.__init__', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Log': ('ops.common.html#log', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Log.__init__': ('ops.common.html#log.__init__', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Log.backward': ('ops.common.html#log.backward', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Matmul': ('ops.common.html#matmul', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Matmul.__init__': ('ops.common.html#matmul.__init__', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Matmul.backward': ('ops.common.html#matmul.backward', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Mul': ('ops.common.html#mul', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Mul.__init__': ('ops.common.html#mul.__init__', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Mul.backward': ('ops.common.html#mul.backward', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Neg': ('ops.common.html#neg', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Neg.__init__': ('ops.common.html#neg.__init__', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Neg.backward': ('ops.common.html#neg.backward', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Pow': ('ops.common.html#pow', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Pow.__init__': ('ops.common.html#pow.__init__', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Pow.backward': ('ops.common.html#pow.backward', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Slice': ('ops.common.html#slice', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Slice.__init__': ('ops.common.html#slice.__init__', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Slice.backward': ('ops.common.html#slice.backward', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Sub': ('ops.common.html#sub', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Sub.__init__': ('ops.common.html#sub.__init__', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Sub.backward': ('ops.common.html#sub.backward', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Sum': ('ops.common.html#sum', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Sum.__init__': ('ops.common.html#sum.__init__', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Sum.backward': ('ops.common.html#sum.backward', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Transpose': ('ops.common.html#transpose', 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Transpose.__init__': ( 'ops.common.html#transpose.__init__',
                                                                                 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.Transpose.backward': ( 'ops.common.html#transpose.backward',
                                                                                 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.UnaryElementwiseOp': ( 'ops.common.html#unaryelementwiseop',
                                                                                 'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.UnaryElementwiseOp.__init__': ( 'ops.common.html#unaryelementwiseop.__init__',
                                                                                          'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.calculate_target_shape': ( 'ops.common.html#calculate_target_shape',
                                                                                     'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.maybe_broadcast_elementwise': ( 'ops.common.html#maybe_broadcast_elementwise',
                                                                                          'tidygrad/ops/common.py'),
                                     'tidygrad.ops.common.maybe_broadcast_matmul': ( 'ops.common.html#maybe_broadcast_matmul',
                                                                                     'tidygrad/ops/common.py')},
            'tidygrad.ops.conv': { 'tidygrad.ops.conv.Pad': ('ops.conv.html#pad', 'tidygrad/ops/conv.py'),
                                   'tidygrad.ops.conv.Pad.__init__': ('ops.conv.html#pad.__init__', 'tidygrad/ops/conv.py'),
                                   'tidygrad.ops.conv.Pad.backward': ('ops.conv.html#pad.backward', 'tidygrad/ops/conv.py')},
            'tidygrad.ops.loss': {},
            'tidygrad.ops.shape': { 'tidygrad.ops.shape.Concat': ('ops.shape.html#concat', 'tidygrad/ops/shape.py'),
                                    'tidygrad.ops.shape.Concat.__init__': ('ops.shape.html#concat.__init__', 'tidygrad/ops/shape.py'),
                                    'tidygrad.ops.shape.Concat.backward': ('ops.shape.html#concat.backward', 'tidygrad/ops/shape.py'),
                                    'tidygrad.ops.shape.Stack': ('ops.shape.html#stack', 'tidygrad/ops/shape.py'),
                                    'tidygrad.ops.shape.Stack.__init__': ('ops.shape.html#stack.__init__', 'tidygrad/ops/shape.py'),
                                    'tidygrad.ops.shape.Stack.backward': ('ops.shape.html#stack.backward', 'tidygrad/ops/shape.py')},
            'tidygrad.optim': { 'tidygrad.optim.Adam': ('optim.html#adam', 'tidygrad/optim.py'),
                                'tidygrad.optim.Adam.__init__': ('optim.html#adam.__init__', 'tidygrad/optim.py'),
                                'tidygrad.optim.Adam.step': ('optim.html#adam.step', 'tidygrad/optim.py'),
                                'tidygrad.optim.Optimizer': ('optim.html#optimizer', 'tidygrad/optim.py'),
                                'tidygrad.optim.Optimizer.__init__': ('optim.html#optimizer.__init__', 'tidygrad/optim.py'),
                                'tidygrad.optim.Optimizer.step': ('optim.html#optimizer.step', 'tidygrad/optim.py'),
                                'tidygrad.optim.Optimizer.zero_grad': ('optim.html#optimizer.zero_grad', 'tidygrad/optim.py'),
                                'tidygrad.optim.SGD': ('optim.html#sgd', 'tidygrad/optim.py'),
                                'tidygrad.optim.SGD.__init__': ('optim.html#sgd.__init__', 'tidygrad/optim.py'),
                                'tidygrad.optim.SGD.step': ('optim.html#sgd.step', 'tidygrad/optim.py')},
            'tidygrad.tensor': { 'tidygrad.tensor.Tensor': ('tensor.html#tensor', 'tidygrad/tensor.py'),
                                 'tidygrad.tensor.Tensor.__add__': ('tensor.html#tensor.__add__', 'tidygrad/tensor.py'),
                                 'tidygrad.tensor.Tensor.__del__': ('tensor.html#tensor.__del__', 'tidygrad/tensor.py'),
                                 'tidygrad.tensor.Tensor.__getitem__': ('tensor.html#tensor.__getitem__', 'tidygrad/tensor.py'),
                                 'tidygrad.tensor.Tensor.__init__': ('tensor.html#tensor.__init__', 'tidygrad/tensor.py'),
                                 'tidygrad.tensor.Tensor.__mul__': ('tensor.html#tensor.__mul__', 'tidygrad/tensor.py'),
                                 'tidygrad.tensor.Tensor.__neg__': ('tensor.html#tensor.__neg__', 'tidygrad/tensor.py'),
                                 'tidygrad.tensor.Tensor.__pow__': ('tensor.html#tensor.__pow__', 'tidygrad/tensor.py'),
                                 'tidygrad.tensor.Tensor.__radd__': ('tensor.html#tensor.__radd__', 'tidygrad/tensor.py'),
                                 'tidygrad.tensor.Tensor.__repr__': ('tensor.html#tensor.__repr__', 'tidygrad/tensor.py'),
                                 'tidygrad.tensor.Tensor.__rmul__': ('tensor.html#tensor.__rmul__', 'tidygrad/tensor.py'),
                                 'tidygrad.tensor.Tensor.__rsub__': ('tensor.html#tensor.__rsub__', 'tidygrad/tensor.py'),
                                 'tidygrad.tensor.Tensor.__sub__': ('tensor.html#tensor.__sub__', 'tidygrad/tensor.py'),
                                 'tidygrad.tensor.Tensor.__truediv__': ('tensor.html#tensor.__truediv__', 'tidygrad/tensor.py'),
                                 'tidygrad.tensor.Tensor.accum_grad': ('tensor.html#tensor.accum_grad', 'tidygrad/tensor.py'),
                                 'tidygrad.tensor.Tensor.add': ('tensor.html#tensor.add', 'tidygrad/tensor.py'),
                                 'tidygrad.tensor.Tensor.backward': ('tensor.html#tensor.backward', 'tidygrad/tensor.py'),
                                 'tidygrad.tensor.Tensor.broadcast': ('tensor.html#tensor.broadcast', 'tidygrad/tensor.py'),
                                 'tidygrad.tensor.Tensor.div': ('tensor.html#tensor.div', 'tidygrad/tensor.py'),
                                 'tidygrad.tensor.Tensor.equal': ('tensor.html#tensor.equal', 'tidygrad/tensor.py'),
                                 'tidygrad.tensor.Tensor.exp': ('tensor.html#tensor.exp', 'tidygrad/tensor.py'),
                                 'tidygrad.tensor.Tensor.log': ('tensor.html#tensor.log', 'tidygrad/tensor.py'),
                                 'tidygrad.tensor.Tensor.mean': ('tensor.html#tensor.mean', 'tidygrad/tensor.py'),
                                 'tidygrad.tensor.Tensor.mmul': ('tensor.html#tensor.mmul', 'tidygrad/tensor.py'),
                                 'tidygrad.tensor.Tensor.mul': ('tensor.html#tensor.mul', 'tidygrad/tensor.py'),
                                 'tidygrad.tensor.Tensor.neg': ('tensor.html#tensor.neg', 'tidygrad/tensor.py'),
                                 'tidygrad.tensor.Tensor.pow': ('tensor.html#tensor.pow', 'tidygrad/tensor.py'),
                                 'tidygrad.tensor.Tensor.requires_grad': ('tensor.html#tensor.requires_grad', 'tidygrad/tensor.py'),
                                 'tidygrad.tensor.Tensor.shape': ('tensor.html#tensor.shape', 'tidygrad/tensor.py'),
                                 'tidygrad.tensor.Tensor.split': ('tensor.html#tensor.split', 'tidygrad/tensor.py'),
                                 'tidygrad.tensor.Tensor.std': ('tensor.html#tensor.std', 'tidygrad/tensor.py'),
                                 'tidygrad.tensor.Tensor.sub': ('tensor.html#tensor.sub', 'tidygrad/tensor.py'),
                                 'tidygrad.tensor.Tensor.sum': ('tensor.html#tensor.sum', 'tidygrad/tensor.py'),
                                 'tidygrad.tensor.Tensor.transpose': ('tensor.html#tensor.transpose', 'tidygrad/tensor.py'),
                                 'tidygrad.tensor.Tensor.zero_grad': ('tensor.html#tensor.zero_grad', 'tidygrad/tensor.py'),
                                 'tidygrad.tensor.no_grad': ('tensor.html#no_grad', 'tidygrad/tensor.py'),
                                 'tidygrad.tensor.no_grad.__enter__': ('tensor.html#no_grad.__enter__', 'tidygrad/tensor.py'),
                                 'tidygrad.tensor.no_grad.__exit__': ('tensor.html#no_grad.__exit__', 'tidygrad/tensor.py'),
                                 'tidygrad.tensor.simplify_trace': ('tensor.html#simplify_trace', 'tidygrad/tensor.py')},
            'tidygrad.tensor_helpers': { 'tidygrad.tensor_helpers.Tensor': ('tensor_helpers.html#tensor', 'tidygrad/tensor_helpers.py'),
                                         'tidygrad.tensor_helpers.mean': ('tensor_helpers.html#mean', 'tidygrad/tensor_helpers.py'),
                                         'tidygrad.tensor_helpers.split': ('tensor_helpers.html#split', 'tidygrad/tensor_helpers.py'),
                                         'tidygrad.tensor_helpers.std': ('tensor_helpers.html#std', 'tidygrad/tensor_helpers.py')},
            'tidygrad.training': { 'tidygrad.training.DictLoggerCallback': ('training.html#dictloggercallback', 'tidygrad/training.py'),
                                   'tidygrad.training.DictLoggerCallback.__init__': ( 'training.html#dictloggercallback.__init__',
                                                                                      'tidygrad/training.py'),
                                   'tidygrad.training.DictLoggerCallback.log': ( 'training.html#dictloggercallback.log',
                                                                                 'tidygrad/training.py'),
                                   'tidygrad.training.DictLoggerCallback.post_all_batches': ( 'training.html#dictloggercallback.post_all_batches',
                                                                                              'tidygrad/training.py'),
                                   'tidygrad.training.DictLoggerCallback.post_calc_loss': ( 'training.html#dictloggercallback.post_calc_loss',
                                                                                            'tidygrad/training.py'),
                                   'tidygrad.training.Learner': ('training.html#learner', 'tidygrad/training.py'),
                                   'tidygrad.training.Learner.__init__': ('training.html#learner.__init__', 'tidygrad/training.py'),
                                   'tidygrad.training.Learner.do_all_batches': ( 'training.html#learner.do_all_batches',
                                                                                 'tidygrad/training.py'),
                                   'tidygrad.training.Learner.do_batch_backward': ( 'training.html#learner.do_batch_backward',
                                                                                    'tidygrad/training.py'),
                                   'tidygrad.training.Learner.do_batch_forward': ( 'training.html#learner.do_batch_forward',
                                                                                   'tidygrad/training.py'),
                                   'tidygrad.training.Learner.do_calc_loss': ('training.html#learner.do_calc_loss', 'tidygrad/training.py'),
                                   'tidygrad.training.Learner.do_epoch': ('training.html#learner.do_epoch', 'tidygrad/training.py'),
                                   'tidygrad.training.Learner.do_fit': ('training.html#learner.do_fit', 'tidygrad/training.py'),
                                   'tidygrad.training.Learner.fit': ('training.html#learner.fit', 'tidygrad/training.py'),
                                   'tidygrad.training.Loss': ('training.html#loss', 'tidygrad/training.py'),
                                   'tidygrad.training.Loss.calc': ('training.html#loss.calc', 'tidygrad/training.py'),
                                   'tidygrad.training.Metric': ('training.html#metric', 'tidygrad/training.py'),
                                   'tidygrad.training.Metric.__init__': ('training.html#metric.__init__', 'tidygrad/training.py'),
                                   'tidygrad.training.Metric.calc': ('training.html#metric.calc', 'tidygrad/training.py'),
                                   'tidygrad.training.MultiClassAccuracy': ('training.html#multiclassaccuracy', 'tidygrad/training.py'),
                                   'tidygrad.training.MultiClassAccuracy.calc': ( 'training.html#multiclassaccuracy.calc',
                                                                                  'tidygrad/training.py'),
                                   'tidygrad.training.ProgressBarCallback': ('training.html#progressbarcallback', 'tidygrad/training.py'),
                                   'tidygrad.training.ProgressBarCallback.__init__': ( 'training.html#progressbarcallback.__init__',
                                                                                       'tidygrad/training.py'),
                                   'tidygrad.training.ProgressBarCallback.post_all_batches': ( 'training.html#progressbarcallback.post_all_batches',
                                                                                               'tidygrad/training.py'),
                                   'tidygrad.training.ProgressBarCallback.post_calc_loss': ( 'training.html#progressbarcallback.post_calc_loss',
                                                                                             'tidygrad/training.py'),
                                   'tidygrad.training.ProgressBarCallback.post_epoch': ( 'training.html#progressbarcallback.post_epoch',
                                                                                         'tidygrad/training.py'),
                                   'tidygrad.training.ProgressBarCallback.pre_all_batches': ( 'training.html#progressbarcallback.pre_all_batches',
                                                                                              'tidygrad/training.py'),
                                   'tidygrad.training.ProgressBarCallback.pre_fit': ( 'training.html#progressbarcallback.pre_fit',
                                                                                      'tidygrad/training.py'),
                                   'tidygrad.training.add_callbacks': ('training.html#add_callbacks', 'tidygrad/training.py'),
                                   'tidygrad.training.denoise': ('training.html#denoise', 'tidygrad/training.py'),
                                   'tidygrad.training.metrics_last_pretty': ('training.html#metrics_last_pretty', 'tidygrad/training.py'),
                                   'tidygrad.training.metrics_names_pretty': ('training.html#metrics_names_pretty', 'tidygrad/training.py'),
                                   'tidygrad.training.one_hot_encode_batch': ('training.html#one_hot_encode_batch', 'tidygrad/training.py'),
                                   'tidygrad.training.plot_metrics': ('training.html#plot_metrics', 'tidygrad/training.py'),
                                   'tidygrad.training.print_metrics': ('training.html#print_metrics', 'tidygrad/training.py'),
                                   'tidygrad.training.print_metrics_header': ( 'training.html#print_metrics_header',
                                                                               'tidygrad/training.py')},
            'tidygrad.utils.data': { 'tidygrad.utils.data.DataLoader': ('utils.data.html#dataloader', 'tidygrad/utils/data.py'),
                                     'tidygrad.utils.data.DataLoader.__init__': ( 'utils.data.html#dataloader.__init__',
                                                                                  'tidygrad/utils/data.py'),
                                     'tidygrad.utils.data.DataLoader.__iter__': ( 'utils.data.html#dataloader.__iter__',
                                                                                  'tidygrad/utils/data.py'),
                                     'tidygrad.utils.data.DataLoader.__len__': ( 'utils.data.html#dataloader.__len__',
                                                                                 'tidygrad/utils/data.py'),
                                     'tidygrad.utils.data.DataLoader.__next__': ( 'utils.data.html#dataloader.__next__',
                                                                                  'tidygrad/utils/data.py'),
                                     'tidygrad.utils.data.DataLoaders': ('utils.data.html#dataloaders', 'tidygrad/utils/data.py'),
                                     'tidygrad.utils.data.DataLoaders.__init__': ( 'utils.data.html#dataloaders.__init__',
                                                                                   'tidygrad/utils/data.py'),
                                     'tidygrad.utils.data.Dataset': ('utils.data.html#dataset', 'tidygrad/utils/data.py'),
                                     'tidygrad.utils.data.Dataset.__getitem__': ( 'utils.data.html#dataset.__getitem__',
                                                                                  'tidygrad/utils/data.py'),
                                     'tidygrad.utils.data.Dataset.__len__': ('utils.data.html#dataset.__len__', 'tidygrad/utils/data.py'),
                                     'tidygrad.utils.data.Dataset.collate_fn': ( 'utils.data.html#dataset.collate_fn',
                                                                                 'tidygrad/utils/data.py'),
                                     'tidygrad.utils.data.Dataset.shuffle': ('utils.data.html#dataset.shuffle', 'tidygrad/utils/data.py'),
                                     'tidygrad.utils.data.download_file': ('utils.data.html#download_file', 'tidygrad/utils/data.py')},
            'tidygrad.utils.datasets': { 'tidygrad.utils.datasets.MNIST': ('utils.datasets.html#mnist', 'tidygrad/utils/datasets.py'),
                                         'tidygrad.utils.datasets.MNIST.__getitem__': ( 'utils.datasets.html#mnist.__getitem__',
                                                                                        'tidygrad/utils/datasets.py'),
                                         'tidygrad.utils.datasets.MNIST.__init__': ( 'utils.datasets.html#mnist.__init__',
                                                                                     'tidygrad/utils/datasets.py'),
                                         'tidygrad.utils.datasets.MNIST.__len__': ( 'utils.datasets.html#mnist.__len__',
                                                                                    'tidygrad/utils/datasets.py'),
                                         'tidygrad.utils.datasets.MNIST.collate_fn': ( 'utils.datasets.html#mnist.collate_fn',
                                                                                       'tidygrad/utils/datasets.py'),
                                         'tidygrad.utils.datasets.MNIST.shuffle': ( 'utils.datasets.html#mnist.shuffle',
                                                                                    'tidygrad/utils/datasets.py'),
                                         'tidygrad.utils.datasets.load_fashion_mnist': ( 'utils.datasets.html#load_fashion_mnist',
                                                                                         'tidygrad/utils/datasets.py'),
                                         'tidygrad.utils.datasets.load_mnist': ( 'utils.datasets.html#load_mnist',
                                                                                 'tidygrad/utils/datasets.py'),
                                         'tidygrad.utils.datasets.mnist_batch_tfm': ( 'utils.datasets.html#mnist_batch_tfm',
                                                                                      'tidygrad/utils/datasets.py')},
            'tidygrad.utils.grad_check': { 'tidygrad.utils.grad_check.grad_check': ( 'utils.grad_check.html#grad_check',
                                                                                     'tidygrad/utils/grad_check.py')}}}
