using Nautilus.Assets;
using Nautilus.Assets.Gadgets;
using Nautilus.Assets.PrefabTemplates;
using Nautilus.Crafting;
using Nautilus.Extensions;
using UnityEngine;

namespace Subnautica_Ultimate_modpack_core.Items.Equipment;

public static class ExcalibutPrefab
{
    public static PrefabInfo Info { get; } = PrefabInfo
        .WithTechType("Excalibut", "Excalibut", "Powerfull sword")
        .WithIcon(SpriteManager.Get(TechType.HeatBlade));

    public static void Register()
    {
        var customPrefab = new CustomPrefab(Info);

        var ExcalibutObj = new CloneTemplate(Info, TechType.HeatBlade);
        ExcalibutObj.ModifyPrefab += obj =>
        {
            var heatBlade = obj.GetComponent<HeatBlade>();
            var Excalibut = obj.AddComponent<Excalibut>().CopyComponent(heatBlade);
            Object.DestroyImmediate(heatBlade);
            Excalibut.damage *= 10f;
        };
        customPrefab.SetGameObject(ExcalibutObj);
		var recipe = new RecipeData(new Ingredient(TechType.HeatBlade, 1), new Ingredient(TechType.Gold, 20), new Ingredient(TechType.Lithium, 4), new Ingredient(TechType.PrecursorIonCrystal, 1), new Ingredient(TechType.PrecursorIonPowerCell, 1), new Ingredient(TechType.PlasteelIngot, 2), new Ingredient(TechType.Kyanite, 2), new Ingredient(TechType.Benzene, 1), new Ingredient(TechType.Nickel, 3));
        customPrefab.SetRecipe(recipe)
			.WithFabricatorType(CraftTree.Type.Workbench);
        customPrefab.SetEquipment(EquipmentType.Hand);
        customPrefab.Register();
    }
}

public class Excalibut : HeatBlade
{
    public float hitForce = 5;
    public ForceMode forceMode = ForceMode.Acceleration;
    
    public override string animToolName { get; } = TechType.HeatBlade.AsString(true);

    public override void OnToolUseAnim(GUIHand hand)
    {
        base.OnToolUseAnim(hand);
        
        GameObject hitObj = null;
        Vector3 hitPosition = default;
        UWE.Utils.TraceFPSTargetPosition(Player.main.gameObject, attackDist, ref hitObj, ref hitPosition);
        if (!hitObj)
        {
            // Nothing is in our attack range. Exit method.
            return;
        }

        var liveMixin = hitObj.GetComponentInParent<LiveMixin>();
        if (liveMixin && IsValidTarget(liveMixin))
        {
            var rigidbody = hitObj.GetComponentInParent<Rigidbody>();
            
            if (rigidbody)
            {
                rigidbody.AddForce(MainCamera.camera.transform.forward * hitForce, forceMode);
            }
        }
    }
}