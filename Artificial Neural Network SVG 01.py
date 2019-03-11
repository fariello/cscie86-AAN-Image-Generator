
# coding: utf-8

# In[1]:


import svgwrite
from svgwrite import cm, mm, px


# In[2]:


class DrawingObject(object):
    def __init__(x,y):
        self.x = 0
        self.y = 0
        pass
    
class Node(object):
    d = 20.0
    r = 10.0
    noisy = 3
    num=0
    types = {
        'input': {
            'fg':'#FFCC00',
            'bg':'#663300',
        },
        'input2': {
            'fg':'#FFCC00',
            'bg':'#663300',
        },
        'output': {
            'fg':'#66CC00',
            'bg':'#336600',
        },
        'hidden': {
            'fg':'#CCCCCC',
            'bg':'#333333',
        },
        'other1': {
            'fg':'#CC00FF',
            'bg':'#330066',
        },
        'other2': {
            'fg':'#0099FF',
            'bg':'#003366',            
        },
    }
    
    def __init__(self,x,y,t,st,name=None):
        if name is None:
            name = t
            pass
        self.name = name
        self.self = False
        self.type = t
        self.subtype = st
        self.fg = Node.types[self.type]['bg']
        self.bg = Node.types[self.type]['fg']
        Node.num += 1
        self.num = Node.num
        self.id = id="node%04d" %(self.num)
        pass
    
    def get(self,dwg,num=None):
        g = dwg.g(id="grp_%s" %(self.id))
        if self.self:
            self_loop = dwg.circle(center=(self.x,self.y - Node.r),
                                   r=Node.r/2.0,fill='none',stroke='#333333',
                                   stroke_width=2.0, stroke_opacity=0.66)
            g.add(self_loop)
            pass
        if 'input' == self.type:
            q = (3.0/4.0)*Node.r
            node = dwg.rect((self.x-q,self.y-q),(q*2, q*2),fill=self.bg)
        else:
            node = dwg.circle(center=(self.x,self.y),r=Node.r,fill=self.bg)
            pass
        g.add(node)
        if 1 == self.subtype:
            symbol = dwg.circle(center=(self.x,self.y),r=Node.r/2.0,fill='none',stroke=self.fg,stroke_width=2.0)
            g.add(symbol)
            pass
        elif 2 == self.subtype:
            symbol = dwg.rect((self.x - Node.r/4.0 ,self.y - Node.r/4.0),(Node.r/2.0,Node.r/2.0),fill='none',
                              stroke=self.fg,stroke_width=2.0)
            g.add(symbol)
            pass
        elif Node.noisy == self.subtype:
            q = Node.r/4.0
            x = self.x-(q*2)
            x_max = self.x+(q*3)
            y1 = self.y+q
            y2 = self.y-q
            y = y1
            d=["M"]
            while x < x_max:
                d.append(x)
                d.append(y)
                if y1 == y:
                    y = y2
                else:
                    y = y1
                    pass
                x += q
                pass
            symbol = dwg.path(tuple(d),fill='none',stroke=self.fg,stroke_width=2.0)
            g.add(symbol)
            pass
        if num is not None:
            q = (3.0/4.0)*Node.r
            x = self.x + q
            y = self.y + q + (Node.r/4.0)
            text = dwg.text("%s" %(num),insert=(x,y),
                            style="font-size:6px;font-family:Arial;stroke:white;stroke-width:1;fill:white",
                           )
            g.add(text)
            text = dwg.text("%s" %(num),insert=(x,y),
                            style="font-size:6px;font-family:Arial;stroke:black;stroke-width:0.25;fill:black",
                           )
            g.add(text)
            pass
        return g
        pass

    def center(self,x,y):
        self.x = x
        self.y = y
    pass

class Input(Node):
    def __init__(self,x=0,y=0):
        super().__init__(x,y,'input',0,'Input')
        pass
    pass

class BackfedInput(Node):
    def __init__(self,x=0,y=0):
        super().__init__(x,y,'input',1,'Backfed Input')
        pass
    pass

class BackfedNode(Node):
    def __init__(self,x=0,y=0):
        super().__init__(x,y,'input2',1,'Backfed Input')
        pass
    pass

class NoisyInput(Node):
    def __init__(self,x=0,y=0):
        super().__init__(x,y,'input',Node.noisy,'Noisy Input')
        pass
    pass

class NoisyNode(Node):
    def __init__(self,x=0,y=0):
        super().__init__(x,y,'input2',Node.noisy,'Noisy Node')
        pass
    pass

class OutputNode(Node):
    def __init__(self,x=0,y=0):
        super().__init__(x,y,'output',0,'Output Node')
        pass
    pass

class MatchOutputNode(Node):
    def __init__(self,x=0,y=0):
        super().__init__(x,y,'output',2,'Match Output Node')
        pass
    pass

class HiddenNode(Node):
    def __init__(self,x=0,y=0):
        super().__init__(x,y,'hidden',0,'Hidden Node')
        pass
    pass

class ProbabilisticHiddenNode(Node):
    def __init__(self,x=0,y=0):
        super().__init__(x,y,'hidden',1,'Probabilistic Hidden Node')
        pass
    pass

class SpikingHiddenNode(Node):
    def __init__(self,x=0,y=0):
        super().__init__(x,y,'hidden',2,'Spiking Hidden Node')
        pass
    pass

class RecurrentNode(Node):
    def __init__(self,x=0,y=0):
        super().__init__(x,y,'other1',0,'Recurrent Node')
        self.self = True
        pass
    pass

class MemoryNode(Node):
    def __init__(self,x=0,y=0):
        super().__init__(x,y,'other1',1,'Memory Node')
        self.self = True
        pass
    pass

class DifferentMemoryNode(Node):
    def __init__(self,x=0,y=0):
        super().__init__(x,y,'other1',2,'Different Memory Node')
        self.self = True
        pass
    pass

class KernelNode(Node):
    def __init__(self,x=0,y=0):
        super().__init__(x,y,'other2',2,'Kernel Node')
        pass
    pass

class ConvolutionalNode(Node):
    def __init__(self,x=0,y=0):
        super().__init__(x,y,'other2',1,'Convolutional or Pool Node')
        pass
    pass

class Layer(DrawingObject):
    def __init__(self,num):
        pass

class Network(object):
    def __init__(self,name,id,defstr=None):
        self.id = id
        self.name = name
        self.current_layer = []
        self.layers = [self.current_layer]
        if defstr is not None:
            self.mk(defstr)
        pass

    def new_layer(self):
        self.current_layer = []
        self.layers.append(self.current_layer)
        pass

    def add_node(self,node):
        self.current_layer.append(node)
        pass

    def max_layer_size(self):
        max_layer_size = 0
        for layer in self.layers:
            if len(layer) > max_layer_size:
                max_layer_size = len(layer)
                pass
            pass
        return max_layer_size

    def layer_height(self,layer_size):
        if 0 == layer_size:
            return 0.0
        if 1 == layer_size:
            return Node.d
        return ((layer_size * 2.0) - 1.0 ) * Node.d

    def mk(self,defstr):
        n = 0
        for s in defstr:
            n += 1
            if 'i' == s:
                self.add_node(Input())
            elif 'b' == s:
                self.add_node(BackfedInput())
            elif 'B' == s:
                self.add_node(BackfedNode())
            elif 'n' == s:
                self.add_node(NoisyInput())
            elif 'N' == s:
                self.add_node(NoisyNode())
            elif 'o' == s:
                self.add_node(OutputNode())
            elif 'M' == s:
                self.add_node(MatchOutputNode())
            elif 'h' == s:
                self.add_node(HiddenNode())
            elif 'p' == s:
                self.add_node(ProbabilisticHiddenNode())
            elif 's' == s:
                self.add_node(SpikingHiddenNode())
            elif 'r' == s:
                self.add_node(RecurrentNode())
            elif 'm' == s:
                self.add_node(MemoryNode())
            elif 'd' == s:
                self.add_node(DifferentMemoryNode())
            elif 'k' == s:
                self.add_node(KernelNode())
            elif 'c' == s:
                self.add_node(ConvolutionalNode())
            elif '|' == s:
                self.new_layer()
            else:
                raise ValueError("Don't know what '%s' is." %(s))
                pass
            pass
        pass

    def draw(self,number_nodes=False):
        max_layer_size = self.max_layer_size()
        max_layer_height = self.layer_height(max_layer_size)
        net_x_middle = max_layer_height / 2.0
        width = (len(self.layers)+1) * Node.d * 2.0
        height = max_layer_height + Node.d
        bottom = height
        left = Node.d
        self.filename = "ANN-%s.svg" %(self.name)
        dwg = svgwrite.Drawing(
            filename=self.filename,
            debug=True,
            size=(width,height),
            style="font-size:6px;font-family:Arial;stroke:#999999;stroke-width:0.25;fill:none",
        )
        self.g = dwg.g(id=self.id)
        #self.g.add(dwg.title(self.name))
        layer_num = -1
        svg_layers = []
        svg_lines = []
        n = 0
        for layer in self.layers:
            layer_num += 1
            layer_size = len(layer)
            n += layer_size
            layer_height = self.layer_height(layer_size)
            layer_bottom = bottom - Node.d - net_x_middle + (layer_height / 2.0)
            layer_group = dwg.g(id="%s_l%d" %(self.id, layer_num))
            node_count = -1
            x = left + (layer_num * 2 * Node.d)
            for node in layer:
                node_count += 1
                y = layer_bottom - (node_count * 2 * Node.d)
                node.center(x,y)
                #print("%s (%s,%s)" %(node.name, node.x, node.y))
                if number_nodes:
                    svg_node = node.get(dwg, n)
                else:
                    svg_node = node.get(dwg)
                    pass
                #print(svg_node.tostring())
                layer_group.add(svg_node)
                n -= 1
                pass
            svg_layers.append(layer_group)
            n += layer_size
            pass
        cur_idx = 1
        while cur_idx < 20 and cur_idx < len(self.layers):
            prev_idx = cur_idx - 1
            for start_node in self.layers[prev_idx]:
                start_x = start_node.x
                start_y = start_node.y
                for end_node in self.layers[cur_idx]:
                    end_x = end_node.x
                    end_y = end_node.y
                    line = dwg.line(start=(start_x,start_y),end=(end_x,end_y),stroke='#333333',
                                    stroke_width=2.0, stroke_opacity=0.66)
                    #print(line.tostring())
                    self.g.add(line)
                    pass
                pass
            cur_idx += 1
            pass
        for svg_layer in svg_layers:
            self.g.add(svg_layer)
        dwg.add(self.g)
        print("Saving %s" %(self.filename))
        dwg.save()
        pass
    pass


# In[7]:



net = Network("Test",'test',"iii|bbb|nnn|hhh|ppp|sss|rrr|mmm|ddd|kkk|ccc|MMM|ooo").draw()
net = Network("Legend",'legend',"oMckdmrsphnbi").draw()
net = Network("Perceptron",'P',"iiii|o").draw()
net = Network("Feed Forward",'FF',"ii|hh|o").draw()
net = Network("Radial Basis Network",'RBN',"ii|hh|o").draw()
net = Network("Deep Feed Forward",'DFF',"iii|hhhh|hhhh|oo").draw()
net = Network("Deep Feed Forward 2",'DFF',"iiiiiiiii|hhhhhh|hhhhhh|hhhhhh|hhhhhh|hhhh|oo").draw()
net = Network("Recurrent Neural Network",'RNN',"iii|rrr|rrr|ooo").draw()
net = Network("Recurrent Neural Network 2",'RNN',"iiiii|hhhhh|rrrrr|rrrrr|rrrrr|rrrrr|hhhhh|oo").draw()
net = Network("Long-Short Term Memory Network",'LSTM',"iii|mmm|mmm|ooo").draw()
net = Network("Gated Recurrent Unit Network",'GRU',"iii|ddd|ddd|ooo").draw()
net = Network("Deep Convolutional Network",'DCN',"iiiii|kkkkk|cccc|ccc|cc|hhhh|hhhh|ooo").draw()
net = Network("Deep Convolutional Network 2",'DCN',"iiiii|hhhhh|kkkkk|cccc|ccc|cc|hhhh|hhhh|ooo").draw()
net = Network("Convolutional Network",'CNN',"iiiii|kkkkk|cccc|ccc|cc|o").draw()
net = Network("Deconvolutional Network",'DN',"ii|ccc|cccc|kkkkk|ooooo").draw()
net = Network("Deconvolutional Network 2",'DN',"ii|cc|ccc|cccc|kkkkk|ooooo").draw()
net = Network("Deep Convolutional Inverse Graphics Network",'DCIGN',"iiiii|kkkkk|cccc|ccc|ppp|ccc|cccc|kkkkk|ooooo").draw()
net = Network("Generative Adversarial Network",'GAN',"bbb|hhh|hhh|MMM|hhh|hhh|MM").draw()
net = Network("Generative Adversarial Network 2",'GAN',"iii|rrr|hhh|hhh|MMM|hhh|hhh|MM").draw()
net = Network("Liquid State Machine",'LQM',"iii|ssss|ssss|ssss|oo").draw()
net = Network("Extreme Learning Machine",'ELM',"iii|hhhh|hhhh|hhhh|oo").draw()
net = Network("Echo State Network",'ESN',"iii|rrrr|rrrr|rrrr|oo").draw()
net = Network("Autoencoder",'AE',"iiii|hh|MMMM").draw()
net = Network("Autoencoder 2",'AE',"iiiiii|hhhh|hhh|hhhh|MMMMMM").draw()
net = Network("Variational Autoencoder",'VAE',"iiii|pppp|MMMM").draw()
net = Network("Variational Autoencoder 2",'AE',"iiiiii|pppp|ppp|pppp|MMMMMM").draw()
net = Network("Denoising Autencoder",'DAE',"nnnn|hhhh|MMMM").draw()
net = Network("Denoising Autencoder 2",'DAE',"iiiiii|NNNNNN|hhhh|hhh|hhhh|MMMMMM").draw()
net = Network("Sparse Autoencoder",'SAE',"ii|hhhh|MM").draw()
net = Network("Sparse Autoencoder 2",'SAE',"iiiii|hhhhh|hhh|hhhhh|MMMMM").draw()
net = Network("Deep Residual Network",'DSN',"iii|hhh|hhh|hhh|hhh|hhh|hhh|hhh|oo").draw()
net = Network("Kohonen Network",'KN',"ii|hhh|hhh|hhh").draw()
net = Network("Support Vector Machine",'SVN',"iii|hhh|hhh|o").draw()
net = Network("Neural Turing Machine",'NTM',"iii|hh|hh|hhh|mmm|o").draw()
net = Network("Deep Belief Network",'DBN',"bbbb|pp|hhhh|pp|hhhh|pp|MMMM").draw()
net = Network("Deep Belief Network 2",'DBN',"iiii|hhhh|pp|hhhh|pp|hhhh|pp|MMMM").draw()
net = Network("Restricted Boltzmann Machine",'RBM',"bbb|pppp").draw()
net = Network("Restricted Boltzmann Machine 2",'RBM',"iii|hhh|rrrr").draw()
#net = Network("Boltzmann Machine",'BM',"iiiiii|hhhhhh|rrrrrrr").draw()

