import sys
from typing import *
from torch import Tensor

from gradio.components import Component

from k_diffusion.external import CompVisDenoiser
from ldm.models.diffusion.ddpm import LatentDiffusion

from modules.processing import StableDiffusionProcessing as Processing, StableDiffusionProcessingImg2Img as ProcessingImg2Img, Processed
from modules.prompt_parser import MulticondLearnedConditioning, ScheduledPromptConditioning
from modules.extra_networks import ExtraNetworkParams
from modules.sd_samplers_kdiffusion import KDiffusionSampler, CFGDenoiser
from modules.sd_samplers_compvis import VanillaStableDiffusionSampler

ModuleType = type(sys)

Sampler = Union[KDiffusionSampler, VanillaStableDiffusionSampler]
Cond = MulticondLearnedConditioning
Uncond = List[List[ScheduledPromptConditioning]]
ExtraNetworkData = DefaultDict[str, List[ExtraNetworkParams]]

# 'c_crossattn': Tensor    # prompt cond
# 'c_concat':    Tensor    # latent mask
# 'c_adm':       Tensor    # unclip
CondDict = Dict[str, Tensor]
