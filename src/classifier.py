import cv2
import numpy as np
from dataclasses import dataclass
from typing import Dict, List, Any


@dataclass
class PlantEntity:
    label: str
    category: str  # CULTIVO, JARDIN, MALEZA
    area_coverage_pct: float
    recommended_action: str


class AgroDronClassifier:
    """
    Módulo de Visión para AgroDron v2.2.
    Segmentación por espacio HSV, catálogo taxonómico y cálculo del IPC.
    """

    CATALOG = {
        # Cultivos Agrícolas
        'frijol_guia': {'type': 'CULTIVO', 'leaf_type': 'trifoliate', 'has_stakes': True},
        'maiz_sorgo': {'type': 'CULTIVO', 'leaf_type': 'linear_broad', 'water_risk': 'high'},
        'nopal': {'type': 'CULTIVO', 'leaf_type': 'cladode', 'water_risk': 'critical'},
        'cana_azucar': {'type': 'CULTIVO', 'leaf_type': 'linear_tall', 'water_risk': 'medium'},
        'camote_campanilla': {'type': 'CULTIVO', 'leaf_type': 'cordate_creeping', 'water_risk': 'medium'},
        
        # Plantas de Jardín
        'adenium': {'type': 'JARDIN', 'leaf_type': 'caudex_succulent', 'container': True},
        'verdolaga': {'type': 'JARDIN', 'leaf_type': 'succulent_mat', 'container': False},
        
        # Malezas
        'bidens_pilosa': {'type': 'MALEZA', 'competition': 'high', 'action': 'remover'},
        'commelina': {'type': 'MALEZA', 'indicator': 'waterlogging', 'action': 'drenar_y_remover'},
        'zacates_pastos': {'type': 'MALEZA', 'competition': 'medium', 'action': 'control_mecanico'}
    }

    def process_frame(self, image_bgr: np.ndarray) -> Dict[str, float]:
        """
        Calcula el porcentaje total de cobertura vegetativa viva usando el espacio HSV.
        """
        hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)
        
        # Rango de verde para cobertura vegetativa viva
        lower_green = np.array([30, 40, 40])
        upper_green = np.array([85, 255, 255])
        green_mask = cv2.inRange(hsv, lower_green, upper_green)

        total_pixels = image_bgr.shape[0] * image_bgr.shape[1]
        green_pixels = cv2.countNonZero(green_mask)

        coverage_pct = (green_pixels / total_pixels) * 100
        return {"vegetation_coverage_pct": round(coverage_pct, 2)}

    def evaluate_ipc(self, weed_area_pct: float, total_veg_pct: float) -> Dict[str, Any]:
        """
        Calcula el Índice de Presión de Competencia (IPC) y determina la acción agronómica.
        IPC = (Área Ocupada por Malezas / Área Total Vegetada) * 100
        """
        if total_veg_pct <= 0:
            return {
                "ipc_pct": 0.0,
                "risk_level": "LOW",
                "action": "Vuelo estándar de monitoreo (30 m). Sin aplicación."
            }

        ipc = (weed_area_pct / total_veg_pct) * 100

        if ipc < 20.0:
            risk = "LOW"
            action = "Vuelo estándar de monitoreo (30 m). Sin aplicación."
        elif 20.0 <= ipc <= 50.0:
            risk = "MEDIUM"
            action = "Alerta de Competencia: Deshierbe focalizado/manual."
        else:
            risk = "CRITICAL"
            action = "Intervención Crítica: Control mecánico o térmico urgente."

        return {
            "ipc_pct": round(ipc, 2),
            "risk_level": risk,
            "action": action
        }
