using System.Reflection;
using BepInEx;
using BepInEx.Logging;
using HarmonyLib;
using Subnautica_Ultimate_modpack_core.Items.Equipment;

namespace Subnautica_Ultimate_modpack_core;

[BepInPlugin("pl.Subnautica_Ultimate_modpack_core", "Subnautica_Ultimate_modpack_core", "1.0.0")]
[BepInDependency("com.snmodding.nautilus")]
public class Plugin : BaseUnityPlugin
{
    public new static ManualLogSource Logger { get; private set; }
    
    private static Assembly Assembly { get; } = Assembly.GetExecutingAssembly();
	
    private void Awake()
    {
        Logger = base.Logger;
		
        
        InitializePrefabs();

        Harmony.CreateAndPatchAll(Assembly, "pl.Subnautica_Ultimate_modpack_core");
        Logger.LogInfo("Plugin Subnautica_Ultimate_modpack_core is loaded!");
    }

    private void InitializePrefabs()
    {
        ExcalibutPrefab.Register();
		SkyOfMyWorldPrefab.Register();
		ElectricIonPowerCellPrefab.Register();
    }
}
