# generated by datamodel-codegen:
#   filename:  https://csrc.nist.gov/schema/nvd/api/2.0/external/cvss-v3.0.json
#   timestamp: 2023-03-02T09:53:38+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, confloat, constr


class Version(Enum):
    """
    CVSS Version
    """

    field_3_0 = '3.0'


class AttackVectorType(Enum):
    NETWORK = 'NETWORK'
    ADJACENT_NETWORK = 'ADJACENT_NETWORK'
    LOCAL = 'LOCAL'
    PHYSICAL = 'PHYSICAL'


class ModifiedAttackVectorType(Enum):
    NETWORK = 'NETWORK'
    ADJACENT_NETWORK = 'ADJACENT_NETWORK'
    LOCAL = 'LOCAL'
    PHYSICAL = 'PHYSICAL'
    NOT_DEFINED = 'NOT_DEFINED'


class AttackComplexityType(Enum):
    HIGH = 'HIGH'
    LOW = 'LOW'


class ModifiedAttackComplexityType(Enum):
    HIGH = 'HIGH'
    LOW = 'LOW'
    NOT_DEFINED = 'NOT_DEFINED'


class PrivilegesRequiredType(Enum):
    HIGH = 'HIGH'
    LOW = 'LOW'
    NONE = 'NONE'


class ModifiedPrivilegesRequiredType(Enum):
    HIGH = 'HIGH'
    LOW = 'LOW'
    NONE = 'NONE'
    NOT_DEFINED = 'NOT_DEFINED'


class UserInteractionType(Enum):
    NONE = 'NONE'
    REQUIRED = 'REQUIRED'


class ModifiedUserInteractionType(Enum):
    NONE = 'NONE'
    REQUIRED = 'REQUIRED'
    NOT_DEFINED = 'NOT_DEFINED'


class ScopeType(Enum):
    UNCHANGED = 'UNCHANGED'
    CHANGED = 'CHANGED'


class ModifiedScopeType(Enum):
    UNCHANGED = 'UNCHANGED'
    CHANGED = 'CHANGED'
    NOT_DEFINED = 'NOT_DEFINED'


class CiaType(Enum):
    NONE = 'NONE'
    LOW = 'LOW'
    HIGH = 'HIGH'


class ModifiedCiaType(Enum):
    NONE = 'NONE'
    LOW = 'LOW'
    HIGH = 'HIGH'
    NOT_DEFINED = 'NOT_DEFINED'


class ExploitCodeMaturityType(Enum):
    UNPROVEN = 'UNPROVEN'
    PROOF_OF_CONCEPT = 'PROOF_OF_CONCEPT'
    FUNCTIONAL = 'FUNCTIONAL'
    HIGH = 'HIGH'
    NOT_DEFINED = 'NOT_DEFINED'


class RemediationLevelType(Enum):
    OFFICIAL_FIX = 'OFFICIAL_FIX'
    TEMPORARY_FIX = 'TEMPORARY_FIX'
    WORKAROUND = 'WORKAROUND'
    UNAVAILABLE = 'UNAVAILABLE'
    NOT_DEFINED = 'NOT_DEFINED'


class ConfidenceType(Enum):
    UNKNOWN = 'UNKNOWN'
    REASONABLE = 'REASONABLE'
    CONFIRMED = 'CONFIRMED'
    NOT_DEFINED = 'NOT_DEFINED'


class CiaRequirementType(Enum):
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'
    NOT_DEFINED = 'NOT_DEFINED'


class SeverityType(Enum):
    NONE = 'NONE'
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'
    CRITICAL = 'CRITICAL'


class CveCvssDataModel(BaseModel):
    version: Version = Field(..., description='CVSS Version')
    vectorString: constr(
        regex=r'^CVSS:3[.]0/((AV:[NALP]|AC:[LH]|PR:[UNLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:[XURC]|[CIA]R:[XLMH]|MAV:[XNALP]|MAC:[XLH]|MPR:[XUNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])/)*(AV:[NALP]|AC:[LH]|PR:[UNLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:[XURC]|[CIA]R:[XLMH]|MAV:[XNALP]|MAC:[XLH]|MPR:[XUNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])$'
    )
    attackVector: Optional[AttackVectorType] = None
    attackComplexity: Optional[AttackComplexityType] = None
    privilegesRequired: Optional[PrivilegesRequiredType] = None
    userInteraction: Optional[UserInteractionType] = None
    scope: Optional[ScopeType] = None
    confidentialityImpact: Optional[CiaType] = None
    integrityImpact: Optional[CiaType] = None
    availabilityImpact: Optional[CiaType] = None
    baseScore: confloat(ge=0.0, le=10.0)
    baseSeverity: SeverityType
    exploitCodeMaturity: Optional[ExploitCodeMaturityType] = None
    remediationLevel: Optional[RemediationLevelType] = None
    reportConfidence: Optional[ConfidenceType] = None
    temporalScore: Optional[confloat(ge=0.0, le=10.0)] = None
    temporalSeverity: Optional[SeverityType] = None
    confidentialityRequirement: Optional[CiaRequirementType] = None
    integrityRequirement: Optional[CiaRequirementType] = None
    availabilityRequirement: Optional[CiaRequirementType] = None
    modifiedAttackVector: Optional[ModifiedAttackVectorType] = None
    modifiedAttackComplexity: Optional[ModifiedAttackComplexityType] = None
    modifiedPrivilegesRequired: Optional[ModifiedPrivilegesRequiredType] = None
    modifiedUserInteraction: Optional[ModifiedUserInteractionType] = None
    modifiedScope: Optional[ModifiedScopeType] = None
    modifiedConfidentialityImpact: Optional[ModifiedCiaType] = None
    modifiedIntegrityImpact: Optional[ModifiedCiaType] = None
    modifiedAvailabilityImpact: Optional[ModifiedCiaType] = None
    environmentalScore: Optional[confloat(ge=0.0, le=10.0)] = None
    environmentalSeverity: Optional[SeverityType] = None
