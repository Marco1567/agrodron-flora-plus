import cv2
import numpy as np
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class PlantEntity:
    label: str
    category: str
    area_coverage_pct: float
    recommended_action: str

class AgroDronClassifier:
    """
    Módulo de Visión para AgroDron v2.2.
    Segmentación por espacio HSV y detección de estructuras de vegetación.
    """
    
    CATALOG = {
        'frijol_guia': {'type': 'CULTIVO', 'leaf_type': 'trifoliate', 'has_stakes': True},
        'maiz_sorgo': {'type': 'CULTIVO', 'leaf_type': 'linear_broad', 'water_risk': 'high'},
        'nopal': {'type': 'CULTIVO', 'leaf_type': 'cladode', 'water_risk': 'critical'},
        'adenium': {'type': 'JARDIN', 'leaf_type': 'caudex_succulent', 'container': True},
        'bidens_pilosa': {'type': 'MALEZA', 'competition': 'high', 'action': 'remover'},
        'commelina': {'type': 'MALEZA', 'indicator': 'waterlogging', 'action': 'drenar_y_remover'}
    }

    def process_frame(self, image_bgr: np.ndarray) -> Dict[str, float]:
        hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)
        lower_green = np.array([30, 40, 40])
        upper_green = np.array([85, 255, 255])
        green_mask = cv2.inRange(hsv, lower_green, upper_green)
        
        total_pixels = image_bgr.shape[0] * image_bgr.shape[1]
        green_pixels = cv2.countNonZero(green_mask)
        
        coverage_pct = (green_pixels / total_pixels) * 100
        return {"vegetation_coverage_pct": round(coverage_pct, 2)}
      
