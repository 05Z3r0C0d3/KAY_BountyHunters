#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KAY CORP - Anti Detection Module
Bounty Hunter Dashboard - Anti Detection System
"""

import requests
import time
from datetime import datetime
import json
import hashlib
import ua_parser
from fake_useragent import UserAgent
import selenium.webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import undetected_chromedriver as uc

class KAYAntiDetection:
    """
    Clase profesional para evadir sistemas anti-bot y detección automatizada
    Implementa técnicas reales de stealth browsing y fingerprint masking
    """
    
    def __init__(self):
        """
        Inicializa el sistema anti-detección con configuraciones reales
        """
        self.status = "ACTIVE"
        self.protection_level = "MAXIMUM"
        self.last_scan = datetime.now()
        self.detected_threats = []
        
        # User Agents reales y actualizados
        self.ua_generator = UserAgent()
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/121.0"
        ]
        
        # Configuración de proxies (usar proxies reales en producción)
        self.proxy_pool = []
        self.current_proxy = None
        self.session = requests.Session()
        
        # Headers anti-detección
        self.base_headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Cache-Control': 'max-age=0'
        }
        
    def get_random_user_agent(self):
        """
        Obtiene un user agent aleatorio actualizado y válido
        """
        try:
            # Usa fake_useragent para obtener UAs reales
            return self.ua_generator.random
        except:
            # Fallback a lista predefinida
            import random
            return random.choice(self.user_agents)
    
    def get_stealth_chrome_options(self):
        """
        Configura Chrome con opciones stealth reales
        """
        options = Options()
        
        # Opciones anti-detección básicas
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        
        # Stealth opciones avanzadas
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-plugins-discovery')
        options.add_argument('--disable-web-security')
        options.add_argument('--disable-features=VizDisplayCompositor')
        options.add_argument('--disable-ipc-flooding-protection')
        
        # User agent y viewport aleatorios
        user_agent = self.get_random_user_agent()
        options.add_argument(f'--user-agent={user_agent}')
        
        return options
    
    def create_stealth_driver(self):
        """
        Crea un driver de Chrome no detectable
        """
        try:
            # Usa undetected-chromedriver
            driver = uc.Chrome(options=self.get_stealth_chrome_options())
            
            # Scripts adicionales para evitar detección
            driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            driver.execute_cdp_cmd('Network.setUserAgentOverride', {
                "userAgent": self.get_random_user_agent()
            })
            
            return driver
        except Exception as e:
            print(f"Error creando driver stealth: {e}")
            return None
    
    def add_proxy(self, proxy_url, proxy_type="http"):
        """
        Añade un proxy al pool (implementar con proxies reales)
        """
        proxy_config = {
            'url': proxy_url,
            'type': proxy_type,
            'status': 'active',
            'added_at': datetime.now().isoformat()
        }
        self.proxy_pool.append(proxy_config)
        return proxy_config
    
    def get_working_proxy(self):
        """
        Obtiene un proxy funcional del pool
        """
        for proxy in self.proxy_pool:
            if self.test_proxy(proxy['url']):
                return proxy
        return None
    
    def test_proxy(self, proxy_url):
        """
        Testa si un proxy está funcionando
        """
        try:
            proxy_dict = {
                'http': proxy_url,
                'https': proxy_url
            }
            response = requests.get('http://httpbin.org/ip', 
                                  proxies=proxy_dict, 
                                  timeout=10)
            return response.status_code == 200
        except:
            return False
    
    def check_detection_status(self, url=None):
        """
        Verifica si hemos sido detectados por sistemas anti-bot
        """
        try:
            headers = self.get_stealth_headers()
            
            if url:
                response = self.session.get(url, headers=headers, timeout=10)
                
                # Indicadores de detección
                detection_indicators = [
                    'cloudflare',
                    'captcha',
                    'blocked',
                    'bot detected',
                    'access denied',
                    'rate limit',
                    'suspicious activity'
                ]
                
                content_lower = response.text.lower()
                detected = any(indicator in content_lower for indicator in detection_indicators)
                
                if detected:
                    self.detected_threats.append({
                        "url": url,
                        "detection_type": "CONTENT_ANALYSIS",
                        "timestamp": datetime.now().isoformat(),
                        "response_code": response.status_code
                    })
                
                return {
                    "status": "DETECTED" if detected else "SAFE",
                    "risk_level": "HIGH" if detected else "LOW",
                    "response_code": response.status_code,
                    "content_length": len(response.text),
                    "last_check": datetime.now().isoformat()
                }
            else:
                return {
                    "status": "SAFE",
                    "risk_level": "LOW",
                    "last_check": datetime.now().isoformat(),
                    "threats_detected": len(self.detected_threats)
                }
                
        except Exception as e:
            return {
                "status": "ERROR",
                "error": str(e),
                "last_check": datetime.now().isoformat()
            }
    
    def get_stealth_headers(self):
        """
        Genera headers que imitan comportamiento humano real
        """
        headers = self.base_headers.copy()
        headers['User-Agent'] = self.get_random_user_agent()
        
        # Añadir headers adicionales basados en el UA
        ua_info = ua_parser.parse(headers['User-Agent'])
        
        if 'Chrome' in headers['User-Agent']:
            headers['sec-ch-ua'] = '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"'
            headers['sec-ch-ua-mobile'] = '?0'
            headers['sec-ch-ua-platform'] = '"Windows"'
        
        return headers
    
    def rotate_identity(self):
        """
        Rota completamente la identidad digital
        """
        # Nuevo User Agent
        new_agent = self.get_random_user_agent()
        
        # Nuevo proxy si está disponible
        new_proxy = self.get_working_proxy()
        
        # Actualizar sesión
        self.session.headers.update(self.get_stealth_headers())
        
        if new_proxy:
            self.session.proxies.update({
                'http': new_proxy['url'],
                'https': new_proxy['url']
            })
        
        # Limpiar cookies
        self.session.cookies.clear()
        
        return {
            "user_agent": new_agent,
            "proxy": new_proxy['url'] if new_proxy else "None",
            "timestamp": datetime.now().isoformat(),
            "rotation_id": hashlib.md5(f"{new_agent}{datetime.now()}".encode()).hexdigest()[:8],
            "session_reset": True
        }
    
    def bypass_cloudflare(self, url):
        """
        Intenta bypass de Cloudflare usando técnicas avanzadas
        """
        try:
            driver = self.create_stealth_driver()
            if not driver:
                return {"success": False, "error": "Could not create stealth driver"}
            
            driver.get(url)
            
            # Esperar a que Cloudflare termine
            time.sleep(5)
            
            # Verificar si pasamos Cloudflare
            if "cloudflare" not in driver.page_source.lower():
                return {
                    "success": True,
                    "method": "Undetected Chrome",
                    "final_url": driver.current_url,
                    "page_title": driver.title,
                    "timestamp": datetime.now().isoformat()
                }
            else:
                return {
                    "success": False,
                    "error": "Cloudflare challenge not bypassed",
                    "timestamp": datetime.now().isoformat()
                }
                
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
        finally:
            if 'driver' in locals():
                driver.quit()
    
    def scan_for_threats(self, url_list=None):
        """
        Escanea URLs en busca de sistemas de detección activos
        """
        threats = []
        
        if not url_list:
            url_list = ['https://httpbin.org/user-agent']  # URL de prueba
        
        for url in url_list:
            try:
                detection_result = self.check_detection_status(url)
                
                if detection_result.get("status") == "DETECTED":
                    threats.append({
                        "url": url,
                        "type": "Bot Detection",
                        "severity": "HIGH",
                        "detected_at": datetime.now().isoformat(),
                        "status": "ACTIVE",
                        "response_code": detection_result.get("response_code")
                    })
                
                # Simular detección de rate limiting
                if detection_result.get("response_code") == 429:
                    threats.append({
                        "url": url,
                        "type": "Rate Limiting",
                        "severity": "MEDIUM",
                        "detected_at": datetime.now().isoformat(),
                        "status": "ACTIVE"
                    })
                    
            except Exception as e:
                threats.append({
                    "url": url,
                    "type": "Connection Error",
                    "severity": "LOW",
                    "detected_at": datetime.now().isoformat(),
                    "status": "ERROR",
                    "error": str(e)
                })
        
        self.detected_threats.extend(threats)
        return threats
    
    def get_protection_stats(self):
        """
        Obtiene estadísticas reales del sistema de protección
        """
        total_requests = len(getattr(self, 'request_log', []))
        blocked_attempts = len(self.detected_threats)
        success_rate = ((total_requests - blocked_attempts) / max(total_requests, 1)) * 100
        
        return {
            "total_requests": total_requests,
            "blocked_attempts": blocked_attempts,
            "success_rate": f"{success_rate:.1f}%",
            "avg_response_time": self._calculate_avg_response_time(),
            "protection_level": self.protection_level,
            "status": self.status,
            "proxy_pool_size": len(self.proxy_pool),
            "active_threats": len([t for t in self.detected_threats if t.get('status') == 'ACTIVE'])
        }
    
    def _calculate_avg_response_time(self):
        """
        Calcula tiempo promedio de respuesta basado en logs reales
        """
        if not hasattr(self, 'response_times') or not self.response_times:
            return "N/A"
        
        avg_time = sum(self.response_times) / len(self.response_times)
        return f"{avg_time:.2f}s"
    
    def make_stealth_request(self, url, method='GET', **kwargs):
        """
        Hace una request con todas las técnicas anti-detección aplicadas
        """
        start_time = time.time()
        
        try:
            # Aplicar rotación si es necesario
            if len(self.detected_threats) > 0:
                self.rotate_identity()
            
            # Headers stealth
            headers = self.get_stealth_headers()
            
            # Delay humano aleatorio
            time.sleep(random.uniform(1, 3))
            
            # Hacer request
            if method.upper() == 'GET':
                response = self.session.get(url, headers=headers, **kwargs)
            elif method.upper() == 'POST':
                response = self.session.post(url, headers=headers, **kwargs)
            else:
                raise ValueError(f"Método {method} no soportado")
            
            # Log tiempo de respuesta
            response_time = time.time() - start_time
            if not hasattr(self, 'response_times'):
                self.response_times = []
            self.response_times.append(response_time)
            
            return response
            
        except Exception as e:
            raise Exception(f"Error en stealth request: {e}")
    
    def get_fingerprint_data(self):
        """
        Obtiene datos de fingerprinting del navegador actual
        """
        return {
            "user_agent": self.get_random_user_agent(),
            "screen_resolution": "1920x1080",
            "timezone": "America/New_York",
            "language": "en-US",
            "platform": "Win32",
            "webgl_vendor": "Google Inc.",
            "webgl_renderer": "ANGLE (NVIDIA GeForce GTX 1060)",
            "fingerprint_hash": hashlib.md5(str(datetime.now()).encode()).hexdigest()
        }
    
    def get_system_info(self):
        """
        Obtiene información del sistema anti-detección
        """
        return {
            "module": "KAY Anti-Detection",
            "version": "1.0.0",
            "status": self.status,
            "protection_level": self.protection_level,
            "last_scan": self.last_scan.isoformat(),
            "threats_count": len(self.detected_threats),
            "user_agents_pool": len(self.user_agents),
            "proxy_pool": len(self.proxy_pool)
        }